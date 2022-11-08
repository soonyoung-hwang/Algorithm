N = int(input())
M = int(input())
arr = []

for _ in range(M):
    arr.append(list(map(int,input().split())))
    
answer = -1

routes = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    routes[arr[i][0]][arr[i][1]] = 1
    routes[arr[i][1]][arr[i][0]] = 1



visited = [False for i in range(N+1)]

def dfs(v):
    global answer
    if(visited[v] == True):
        return
    
    visited[v] = True
    answer += 1
    remains = []
    for i in range(1,N+1):
        if(routes[v][i] == 1):
            remains.append(i)
            dfs(i)

dfs(1)
print(answer)