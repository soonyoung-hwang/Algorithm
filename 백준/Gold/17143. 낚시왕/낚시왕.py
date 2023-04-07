R, C, M = map(int,input().split())
board = [[[[] for __ in range(C)] for __ in range(R)] for __ in range(2)]   # RxC 의 맵 두개
for __ in range(M):
    # 각 칸 마다 -> 방향 속력 크기
    r, c, s, d, z = map(int,input().split())
    if d == 1 or d == 2:
        s %= (R-1)*2
    else:
        s %= (C-1)*2
    board[0][r-1][c-1].append((s, d, z))


dd = ((-1, 0), (1, 0), (0, 1), (0, -1))

current = 0
nxt = 1
killer = -1
answer = 0

cnt = 0
while killer < C-1:
    # catch first
    killer += 1

    for i in range(R):
        if board[current][i][killer]:
            s, d, z = board[current][i][killer].pop()
            answer += z
            break

    for r in range(R):
        for c in range(C):
            if board[current][r][c]:
                s, d, z = board[current][r][c].pop()
                nr, nc = r + dd[d-1][0] * s, c + dd[d-1][1] * s
                for i in range(2):
                    if nr > R-1:
                        # 벗어난 정도 : nr - (R-1)
                        nr = (R-1) - (nr - (R-1))
                        d = 1
                    elif nr < 0:
                        nr = -nr
                        d = 2
                    elif nc > C-1:
                        nc = (C-1) - (nc - (C-1))
                        d = 4
                    elif nc < 0:
                        nc = -nc
                        d = 3

                if not board[nxt][nr][nc]:
                    board[nxt][nr][nc].append((s, d, z))
                    continue

                if board[nxt][nr][nc] and board[nxt][nr][nc][0][2] < z:
                    board[nxt][nr][nc].pop()
                    board[nxt][nr][nc].append((s, d, z))


    current, nxt = nxt, current

print(answer)