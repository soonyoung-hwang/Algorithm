import sys
from collections import deque
from copy import deepcopy
MAX = sys.maxsize

N, M = map(int,input().split())
board = [list(map(int,input().split())) for __ in range(N)]

goal = 0                    # goal : 맵에 총 퍼져야할 바이러스의 개수
candidate = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            goal += 1
        if board[i][j] == 2:
            candidate.append((i,j))


answer = MAX
L = len(candidate)
dd = ((0, 1), (0, -1), (1, 0), (-1, 0))

def check():
    global goal

    visited = [[0 for __ in range(N)] for __ in range(N)]

    Q = deque(stack[:])
    for virus in stack:
        board[virus[0]][virus[1]] = 3
        visited[virus[0]][virus[1]] = 1

    cnt = 0
    total = 0
    while Q:
        if total == goal:
            return cnt

        for i in range(len(Q)):
            r, c = Q.popleft()
            
            for k in range(4):
                nr, nc = r + dd[k][0], c + dd[k][1]
                if not (0 <= nr < N and 0 <= nc < N): continue
                if visited[nr][nc]: continue
                if board[nr][nc] == 1: continue
                    
                visited[nr][nc] = 1
                if board[nr][nc] == 0:
                    total += 1
                
                Q.append((nr, nc))

        cnt += 1
        

    if total != goal:
        return MAX



stack = []
def dfs(idx, cnt):
    global answer
    if cnt == M:
        answer = min(answer,check())
        for virus in stack:
            board[virus[0]][virus[1]] = 2   # check 에서 활성화 시켰던 것을 다시 비활성화
        
        return
    
    if idx == L:
        return
    
    stack.append(candidate[idx])
    dfs(idx+1, cnt+1)
    stack.pop()
    dfs(idx+1, cnt)
    

dfs(0, 0)
print(answer if answer != MAX else -1)