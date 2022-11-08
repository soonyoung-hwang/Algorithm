import sys,heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
routes = [[] for __ in range(N+1)]
for __ in range(M):
    f, t, c = map(int,input().split())
    routes[f].append([t,c])

A, B = map(int,input().split())

Q = []
Q.append([0, A])
INF = 1e12
dp = [INF] * (N+1)
dp[A] = 0
while Q:
    c, f = heapq.heappop(Q)
    if f == B:
        print(c)
        break
    
    for t, dc in routes[f]:
        if dp[t] > c + dc:
            dp[t] = c + dc
            heapq.heappush(Q,[c+dc, t])