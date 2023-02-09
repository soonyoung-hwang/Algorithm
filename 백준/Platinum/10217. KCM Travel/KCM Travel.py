import heapq
import sys
input = sys.stdin.readline

T = int(input())
for __ in range(T):
    N, M, K = map(int,input().split())
    route = [[] for __ in range(N+1)]
    for __ in range(K):
        a, b, cost, dist = map(int,input().split())
        route[a].append([b, cost, dist])
    
    visited = [[sys.maxsize for __ in range(M+1)] for __ in range(N+1)] # node X cost 의 2차원 배열
    q = [[0, 1, 0]]     # dist, current, cost
    answer = -1
    visited[1][0] = 0

    while q:
        dist, current, cost = heapq.heappop(q)              # [중요] 같은 dist에 대해서, 더 싼 cost가 들어올 수도 있다.
    
        if current == N:
            answer = dist
            break
        
        for n in route[current]:
            _next, c, d = n
            if cost+c > M: continue                         # cost 총 합이 M 이하인 것만 담긴다
            if visited[_next][cost+c] <= dist+d: continue
            for i in range(cost+c, M+1):
                if visited[_next][i] <= dist+d:
                    break
                visited[_next][i] = dist+d

            heapq.heappush(q, [dist+d, _next, cost+c])
    
    print("Poor KCM" if answer == -1 else answer)