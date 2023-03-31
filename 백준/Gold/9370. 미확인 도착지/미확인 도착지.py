from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline
MAX = sys.maxsize

Tc = int(input())

for _ in range(Tc):
    N, M, T = map(int,input().split())
    S, G, H = map(int,input().split())
    routes = [[] for _ in range(N+1)]
    visited = [MAX for _ in range(N+1)]
    possibles = [False for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int,input().split())
        routes[a].append((b, d))
        routes[b].append((a, d))
    
    candidates = [int(input()) for __ in range(T)]




    hq = [(0, 0, S)]    # poss : 0 => 길 아직 안 지남, 1 : 길 지난 상태, 2 : 방금 것이 G-H route 인 경우.
    while hq:
        cost, poss, cur = heapq.heappop(hq)
        if visited[cur] < cost:
            continue

        if visited[cur] == cost:
            if poss != 2:
                continue
            
        if poss:
            np = -1
        else:
            np = 0

        possibles[cur] = np
        visited[cur] = cost


        for nexts, dc in routes[cur]:
            if visited[nexts] < cost+dc:
                continue
            
            elif ((cur,nexts) == (G,H) or (cur,nexts) == (H,G)):
                heapq.heappush(hq, (cost+dc, -2, nexts))

            elif visited[nexts] == cost+dc:
                continue

            else:
                heapq.heappush(hq, (cost+dc, np, nexts))
            
    answer = []
    
    for c in candidates:
        if possibles[c]:
            answer.append(c)

    print(*sorted(answer))