import heapq
import sys
input = sys.stdin.readline

import heapq

N, E = map(int,input().split())
routes = [[] for __ in range(N+1)]
for __ in range(E):
    f, t, c = map(int,input().split())
    routes[f].append([t,c])
    routes[t].append([f,c])

a, b = map(int,input().split())
INF = 1e10

def find_AtoB(A,B):
    Q = []
    Q.append([0, A])
    dp = [INF] * (N+1)
    dp[A] = 0
    while Q:
        c, f = heapq.heappop(Q)

        if f == B:
            break

        for t, dc in routes[f]:
            if dp[t] > c + dc:
                dp[t] = c + dc
                heapq.heappush(Q,[c+dc, t])
    
    return dp[B]


answer = min(find_AtoB(1,a)+find_AtoB(a,b)+find_AtoB(b,N), 
             find_AtoB(1,b)+find_AtoB(b,a)+find_AtoB(a,N))


print(answer if answer < INF else -1)