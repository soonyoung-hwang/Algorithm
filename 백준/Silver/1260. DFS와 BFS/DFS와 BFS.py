N, M, V = map(int,input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))

routes = [[0 for i in range(N+1)] for i in range(N+1)]
for i in range(len(arr)):
    routes[arr[i][0]][arr[i][1]] = 1
    routes[arr[i][1]][arr[i][0]] = 1
    
visited = [False]*(N+1)
# print(routes)

def dfs(v):
    visited[v] = True
    print(v, end = " ")
    remains = []
    for i in range(1,N+1):
        if(routes[v][i] == 1):
            remains.append(i)
    for r in remains:
        if(visited[r] == False):
            dfs(r)

            
def bfs(v):
    visited[v] = True
    c = 1
    print(v, end = " ")
    
    next_set = [v]
    
    while(next_set):
        remains = []
        for i in range(len(next_set)):
            for j in range(1,N+1):
                if(routes[next_set[i]][j] == 1):
                    remains.append(j)
                    
        next_set = []
        for r in remains:
            if(visited[r] == False):
                visited[r] = True
                print(r, end = " ")
                c += 1
                next_set.append(r)
        
        

visited = [False]*(N+1)
dfs(V)
print("")
visited = [False]*(N+1)
bfs(V)