import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    d = arr[x][y]
    nx, ny = np(x,y)
    if not visited[nx][ny]:
        dfs(nx,ny)
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<= nx <= N-1 and 0 <= ny <= M-1 and not visited[nx][ny]):
            if(np(nx,ny) == [x,y]):
                dfs(nx,ny)

def np(x, y):
    # np means next point
    d = arr[x][y]
    if(d == 'D'):
        nx, ny = x+dx[0], y
    elif(d == 'U'):
        nx, ny = x+dx[2], y
    elif(d == 'R'):
        nx, ny = x, y+dy[1]
    else:
        nx, ny = x, y+dy[3]
    
    return [nx, ny]

# print(np(0,0))

N, M = map(int,input().split())
arr = []
for __ in range (N):
    s = input()
    temp = []
    for i in range(M):
        temp.append(s[i])
    arr.append(temp)
    
visited = [[False]*M for __ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if(not visited[i][j]):
            dfs(i,j)
            answer += 1

print(answer)