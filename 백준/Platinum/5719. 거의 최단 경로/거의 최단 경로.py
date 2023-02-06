# 백준 5719 : 거의최단경로

# 거의 최단 경로란 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 것을 말한다. 
# 1. 다익스트라 알고리즘을 통해, 최단경로(들)을 찾는다. 
#  일반적인 다익스트라는 -> 최단 거리만 찾게 된다, 다익스트라를 하면서 각각의 route 들을 저장해주어야 한다.
# 찾았다면, 최단경로(들)에서 쓰여진 모든 경로를 경로별로 -> dictionary로 True / False를 설정한다.
import heapq
import sys
from collections import defaultdict

while True:
    temp_distance = sys.maxsize
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break

    S, D = map(int,input().split())
    routes = [[] for __ in range(N)]
    visited = [sys.maxsize for __ in range(N)]
    closed = dict()

    for __ in range(M):
        a, b, cost = map(int,input().split())
        routes[a].append([b, cost])
        closed[(a,b)] = False
    
    
    paths = defaultdict(list)   # lists of [previous location, current location]
    Q = [[0, S, 0]]     # cost, location, previous
    while Q:
        cost, loc, prev = heapq.heappop(Q)
        if visited[loc] < cost:     # 모든 경로에 대해 최단거리가 아니면 pass 해준다.
            continue

        if [prev, loc] in paths[loc]:
            continue
        
        paths[loc].append([prev, loc])  # 이 path들은, 어디서 왔는지 + 항상 최단거리(들)이므로, backtracking 하다보면 어차피 0으로 이어진다.
        if loc == D:
            if cost <= temp_distance:
                temp_distance = cost

            else: break             # 어디선가 온 path가 최단거리를 벗어난다면, 끝내면 된다.

        for _next in routes[loc]:
            target, c = _next
            if cost+c > visited[target]:
                continue
            visited[target] = cost+c
            heapq.heappush(Q, [cost+c, target, loc])  # new cost, next location, previous location

    second_Q = paths[D]
    while second_Q:
        a, b = second_Q.pop()
        if closed[(a,b)]:
            continue
        closed[(a,b)] = True
        if a == S:
            continue
        for p in paths[a]:
            second_Q.append(p)

    answer = -1
    third_Q = [[0, S]]
    visited = [sys.maxsize for __ in range(N)]
    while third_Q:
        cost, loc = heapq.heappop(third_Q)

        if cost > visited[loc]:
            continue

        if loc == D:
            answer = cost
            break
        
        for _next in routes[loc]:
            target, c = _next
            if closed[(loc, target)]:
                continue
            if cost+c >= visited[target]:
                continue
            visited[target] = cost+c
            heapq.heappush(third_Q,[cost+c, target])

    print(answer)