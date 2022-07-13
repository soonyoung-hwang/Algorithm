start_node = 0
def dfs(cur,visited): 
    """ dp[cur][visited]를 구한 뒤 반환한다. """
    
    if dp[cur][visited] != INF: # 만약 dp[cur][visited]의 값을 이미 구했었다면
        return dp[cur][visited] # 그 값을 반환
    
    if visited == ((1<<(N-1))-1) : # 종단조건 : 만약 모든 노드를 방문한 상태라면 
        if graph[cur][start_node]: # dp[cur][visited] = graph[cur][start_node] 이다. 
            dp[cur][visited] = graph[cur][start_node]
        else: # graph[cur][start_node]에 길이 없다면 INF+1로 업데이트 해준다.(방문했다는 것을 표시)
            dp[cur][visited] = INF+1
        return dp[cur][visited]
    
    
    for i in range(1,N):
        if not graph[cur][i]: # 현재 노드에서 다음 노드까지 길이 없다면 무시
            continue
        if visited & (1<<(i-1)): # 다음 노드가 방문한 노드라면 .. 무시
            continue
        
        dp[cur][visited] = min(dp[cur][visited], graph[cur][i] + dfs(i, visited|1<<(i-1)))
        # 방문하지 않은 노드에 대해서, 현재 노드에서 그 노드로 가는 길이 있다면 dp 값을 업데이트

    if dp[cur][visited] == INF:
        dp[cur][visited] = INF+1 # 만약 모든 노드에 대해새ㅓ 
        # 만약 어떤 노드가 다음노드로 가는 길이 없어서 update가 하나도 되지 않았다면
        # 방문했단 표시로 INF+1을 대입해준다.
        
    return dp[cur][visited]
    
N = int(input())
graph = [list(map(int, input().split())) for __ in range(N)]
INF = 16000000
dp = [[INF for __ in range(1<<(N-1))] for __ in range(N)]
    
print(dfs(0,0)) # 우리가 구하는 값
