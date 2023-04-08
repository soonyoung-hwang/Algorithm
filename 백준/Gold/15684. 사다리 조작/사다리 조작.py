N, M, H = map(int,input().split())
T = (N-1) * H

sadari = [[False for __ in range(N-1)] for __ in range(H)]
for __ in range(M):
    h, n = map(int,input().split())
    sadari[h-1][n-1] = True

def check():
    for s in range(N):
        cur = s
        for h in range(H):
            if cur > 0 and sadari[h][cur-1]:
                cur -= 1

            elif cur < N-1 and sadari[h][cur]:
                cur += 1

        if cur != s:
            return False

    return True

answer = 4
def dfs(idx, cnt):
    global answer
    if cnt >= answer:
        return

    if check():
        answer = cnt
        return

    for ii in range(idx, T):
        h, w = ii // (N - 1), ii % (N - 1)
        if not sadari[h][w]:
            if not sadari[h][max(0, w-1)] and not sadari[h][min(N-2,w+1)]:
                sadari[h][w] = True
                dfs(ii+1, cnt+1)
                sadari[h][w] = False



dfs(0, 0)
print(answer if answer != 4 else -1)