from collections import deque
import sys

dx = [0,-1, 0, 1]
dy = [1, 0,-1, 0]
    
def bfs(x, y, visited):
    Q = deque([[x,y]])
    while Q:
        x, y = Q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if visited[nx][ny] == False and arr[nx][ny] != 0:
                visited[nx][ny] = True
                Q.append([nx,ny])
            elif arr[nx][ny] == 0:
                seas[x][y] += 1

def num_groups(arr):
    count = 0
    visited = [[False]*M for __ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                visited[i][j] == True
                continue
            
            if visited[i][j] == False and count == 0:
                bfs(i,j, visited)
                count += 1
            
            elif visited[i][j] == False and count == 1:
                return 2

    return count
    
def update():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                arr[i][j] = max(0,arr[i][j]-seas[i][j])


N, M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for __ in range(N)]

ans = 0
while True:
    seas = [[0]*M for __ in range(N)]
    t = num_groups(arr)
    if t == 2 or t == 0:
        break
        
    update()
    ans += 1


print(ans if t != 0 else 0)