from collections import deque
import sys
input = sys.stdin.readline

N, M, G, R = map(int,input().split())
board = [list(map(int,input().split())) for __ in range(N)]

candidates = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            candidates.append((i,j))

T = len(candidates)

dd = ((0, 1), (0, -1), (1, 0), (-1, 0))

def in_range(r, c):
    return (0<= r < N and 0 <= c < M)

def check():
    # for i in range(N):
    #     print(*board[i])

    count = 0
    Reds = deque()
    Greens = deque()
    visited_r = [[False for _ in range(M)] for _ in range(N)]
    visited_g = [[False for _ in range(M)] for _ in range(N)]
    is_end = [[False for _ in range(M)] for _ in range(N)]      # 꽃이 피운 땅 : 더 이상 queue에서 처리하면 안 된다.

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'G':
                Greens.append((i,j))
                visited_g[i][j] = True
            elif board[i][j] == 'R':
                Reds.append((i,j))
                visited_r[i][j] = True
    
    end_r, end_g = False, False
    
    # print("Reds :", Reds)
    # print("Greens:", Greens)
    while True:
        new_reds = []
        for i in range(len(Reds)):
            r, c = Reds.popleft()
            if is_end[r][c]: continue

            for d in range(4):
                nr, nc = r + dd[d][0], c + dd[d][1]
                if not in_range(nr,nc): continue
                if visited_r[nr][nc]: continue
                if not board[nr][nc]: continue
                visited_r[nr][nc] = True
                new_reds.append((nr, nc))
                Reds.append((nr, nc))
            
        
        for i in range(len(Greens)):
            r, c = Greens.popleft()
            if is_end[r][c]: continue
            for d in range(4):
                nr, nc = r + dd[d][0], c + dd[d][1]
                if not in_range(nr,nc): continue
                if visited_g[nr][nc]: continue
                if not board[nr][nc]: continue
                visited_g[nr][nc] = True
                if (nr, nc) in new_reds:
                    is_end[nr][nc] = True
                    count += 1
                    continue
                Greens.append((nr, nc))
        
        if not Reds or not Greens:
            break
    
    # print("count :", count)
    return count


def dfs(idx, g_left, r_left):
    global answer
    if g_left == 0 and r_left == 0:
        # chcek path
        answer = max(answer, check())
        return

    if idx == T:
        return
    
    # 해당 땅에 배양액 안 뿌렸을 때
    dfs(idx+1, g_left, r_left)
    
    # 해당 땅에 Green 뿌렸을 때
    r, c = candidates[idx]
    if g_left > 0:
        board[r][c] = 'G'
        dfs(idx+1, g_left-1, r_left)
        board[r][c] = 2

    # 해당 땅에 Red 뿌렸을 때
    if r_left > 0:
        board[r][c] = 'R'
        dfs(idx+1, g_left, r_left-1)
        board[r][c] = 2


answer = 0
dfs(0, G, R)
print(answer)