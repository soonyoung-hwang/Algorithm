# 풀이 : Dijkstra using cost update
from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
routes = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    routes[a].append((b, c))
    routes[b].append((a, c))

costs = [50_000_001 for _ in range(N + 1)]
costs[1] = 0
Q = [(0, 1)]

while Q:
    cost, node = heappop(Q)
    if node == N:
        answer = cost
        break

    for _next, add in routes[node]:
        if costs[_next] <= cost + add:
            continue
        costs[_next] = cost + add
        heappush(Q, (cost + add, _next))


print(answer)