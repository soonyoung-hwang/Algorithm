# 최소비용구하기 2
# 다익스트라 + 경로저장 문제
import heapq
import sys

input = sys.stdin.readline


# system input
N = int(input())
M = int(input())
route = [[] for __ in range(N+1)]
for __ in range(M):
    a, b, cost = map(int,input().split())
    route[a].append([b,cost])
start, dest = map(int,input().split())


# preprocessing
visit_cost = [sys.maxsize for __ in range(N+1)]
tracking = [0 for __ in range(N+1)] # trakcing[i] : previous was i

hQ = [[0, start, 0]]  # [cost, current, previous]

while hQ:
    cost, current, prev = heapq.heappop(hQ)
    if visit_cost[current] <= cost:
        continue
    visit_cost[current] = min(visit_cost[current], cost)
    tracking[current]=prev
    if current == dest:
        break

    for n in route[current]:
        _next, c = n
        if visit_cost[_next] <= cost+c: continue
        heapq.heappush(hQ, [cost+c, _next, current])

s = dest
temp = [dest]
while s != start:
    s = tracking[s]
    temp.append(s)

temp.reverse()
print(visit_cost[dest])
print(len(temp))
print(*temp)