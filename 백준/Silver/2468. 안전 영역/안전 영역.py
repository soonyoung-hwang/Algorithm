import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input()) # 1~100
arr = [list(map(int,input().split())) for __ in range(N)]
visited = [[False for __ in range(N)] for __ in range(N)]


d = ((0,1), (0,-1), (1,0), (-1,0))

def dfs(i,j):
    # find the safe area near the coordinate i, j
    # and make them visited not to count them multiple times
    visited[i][j] = True
    
    x, y = i, j
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if visited[nx][ny]:
            continue
        if arr[nx][ny] <= rain:
            continue
        dfs(nx,ny)
    
def safe_regions(rain):
    # dfs to find safe_regions
    # return number of safe regions
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
                
            visited[i][j] = True
            if arr[i][j] > rain:
                dfs(i,j)
                count += 1
    
    return count

def update_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

answer = 1
for rain in range(1, 100):    
    # update visited
    update_visited()
    answer = max(answer, safe_regions(rain))

print(answer)