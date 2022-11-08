import sys
sys.setrecursionlimit(10**6)

M, N, n = map(int,input().split())
squares = []
for __ in range(n):
    squares.append(list(map(int,input().split())))

arr = [[1]*N for __ in range(M)]
visited = [[False]*N for __ in range(M)]
while(squares):
    s = squares.pop()
    for i in range(s[0],s[2]):
        for j in range(s[1],s[3]):
            arr[j][i] = 0

count = 0    
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x,y):
    global count
    arr[x][y] = 0
    count += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if(0 <= nx <= M-1 and 0 <= ny <= N-1 and arr[nx][ny] == 1):
            dfs(nx,ny)

areas = []
for i in range(M):
    for j in range(N):
        if(arr[i][j] == 1):
            count = 0
            dfs(i,j)
            areas.append(count)

areas.sort()
print(len(areas))
print(*areas)
            
    