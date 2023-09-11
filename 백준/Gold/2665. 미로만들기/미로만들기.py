import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

visited[0][0] = True
Q = deque([[0, 0, 0]])
answer = -1

while Q:
    x, y, c = Q.popleft()
    if x == N-1 and y == N-1:
        answer = c
        break

    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if not in_range(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if board[nx][ny] == 0:
            Q.append([nx, ny, c+1])
        else:
            Q.appendleft([nx, ny, c])
        visited[nx][ny] = True

print(answer)