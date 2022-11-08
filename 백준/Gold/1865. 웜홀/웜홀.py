import sys
input = sys.stdin.readline
INF = 5000001

# 모든 점에 대해 플로이드 와샬로 해당 점에서 목표 점 까지의 최단거리를 구해주고 
# 만약 cycle 이 존재한다면 (만약 존재한다고 하면 무조건 해당 점 까지 음수 값으로 도착할 수 있다.)
# YES 처리를 해주었다.

T = int(input())
for __ in range(T):
    # edges 전처리 : 각 경로에서 cost가 최소인 값만 필요하므로 최소 값으로 업데이트해주고
    # INF가 아닌 숫자들을 모두 edges에 넣어준다.
    
    N, M, W = map(int,input().split())
    routes = [[INF for __ in range(N+1)] for __ in range(N+1)]
    edges = []
    
    for __ in range(M):
        a,b,c = map(int,input().split())
        routes[a][b] = min(routes[a][b], c)
        routes[b][a] = min(routes[b][a], c)
        
    for __ in range(W):
        a,b,c = map(int,input().split())
        routes[a][b] = min(routes[a][b], -c)

        
    for i in range(N+1):
        for j in range(N+1):
            if routes[i][j] != INF:
                edges.append([i,j, routes[i][j]])
    
    flag = False
    visited = [False for __ in range(N+1)] # visited 초기화
    for i in range(1,N+1):
        if flag:
            break
        if visited[i]:
            continue
            
        distance = [INF for __ in range(N+1)]  # distance 초기화
        distance[i] = 0
        visited[i] = True
        for __ in range(N): # 플로이드 와샬 메인
            for edge in edges:
                a,b,c = edge
                if visited[a] and distance[b] > distance[a]+c:
                    distance[b] = distance[a]+c
                    visited[b] = True
                    
        # 만약 한번 더 돌면서 update 되는 경로가 있으면 사이클이 있는 것이므로 flag를 True 해주고 빠져나간다.
        for edge in edges:
            a,b,c = edge
            if visited[a] and distance[b] > distance[a]+c:
                flag = True
                break

    print("YES" if flag else "NO")