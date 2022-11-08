import sys
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if(visited[x][y] != -1):
        return visited[x][y]
    
    ways = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if(0 <= nx <= n-1 and 0 <= ny <= n-1 and arr[x][y] < arr[nx][ny]):
            ways = max(ways, 1+dfs(nx, ny))
    
    visited[x][y] = ways
    return visited[x][y]

n = int(input())
arr = []
for __ in range(n):
    arr.append(list(map(int,input().split())))
    
visited = [[-1]*n for __ in range(n)]
m = 1

for i in range(n):
    for j in range(n):
        m = max(m,dfs(i,j))

print(m)