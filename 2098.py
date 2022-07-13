start_node = 0
def dfs(cur,visited):
    if dp[cur][visited] != INF:
        return dp[cur][visited]
    
    if visited == ((1<<(N-1))-1) :
        if graph[cur][start_node]:
            dp[cur][visited] = graph[cur][start_node]
        else:
            dp[cur][visited] = INF+1
        return dp[cur][visited]
    
    
    for i in range(1,N):
        if not graph[cur][i]:
            continue
        if visited & (1<<(i-1)):
            continue
        dp[cur][visited] = min(dp[cur][visited], graph[cur][i] + dfs(i, visited|1<<(i-1)))

    if dp[cur][visited] == INF:
        dp[cur][visited] = INF+1
        
    return dp[cur][visited]
    
N = int(input())
graph = [list(map(int, input().split())) for __ in range(N)]

INF = 16000000
dp = [[INF for __ in range(1<<(N-1))] for __ in range(N)]
    
print(dfs(0,0))
