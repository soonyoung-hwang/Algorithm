from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

H, W, SR, SC, GR, GC = map(int,input().split())     # width, height, start_row, start_column, goal_row, goal_column

dd = ((0, 1), (1, 0), (0,-1), (-1, 0))
visited = [[False for _ in range(M)] for _ in range(N)]

answer = -1
visited[SR-1][SC-1] = True
Q = deque([(SR-1, SC-1, 0)])

while Q:
    r, c, cnt = Q.popleft()
    

    if r == GR-1 and c == GC-1:
        answer = cnt
        break

    for dr, dc in dd:
        nr, nc = r + dr, c + dc

        if not(0 <= nr < N and 0 <= nc < M):
            continue
        if not(0 <= nr+H <= N and 0 <= nc+W <= M):
            continue
        if visited[nr][nc]:
            continue
        
        visited[nr][nc] = True
        
        # check if the rectangular can move or not
        is_possible = True
        if (dr, dc) == (0, 1):
            for i in range(r, r+H):
                if board[i][c+W]:
                    is_possible = False
                    break
        
        elif (dr, dc) == (1, 0):
            for i in range(c, c+W):
                if board[r+H][i]:
                    is_possible = False
                    break

        elif (dr, dc) == (0, -1):
            for i in range(r, r+H):
                if board[i][nc]:
                    is_possible = False
                    break

        else:
            for i in range(c, c+W):
                if board[nr][i]:
                    is_possible = False
                    break
        
        if is_possible:
            Q.append((nr, nc, cnt+1))

print(answer)