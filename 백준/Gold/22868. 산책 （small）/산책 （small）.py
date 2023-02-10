# 산책(small)
# 백준 2.10 알고리즘 게시판 질문

import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int,input().split())
route = [[] for __ in range(N+1)]
for __ in range(M):
    a, b = map(int,input().split())
    route[a].append(b)
    route[b].append(a)

S, E = map(int,input().split())

for i in range(1, N+1):
    route[i].sort()

previous = [0 for __ in range(N+1)]
closed = [False for __ in range(N+1)]

def dijkstra(s, e):
    visited = [False for __ in range(N+1)]
    Q = deque()
    visited[s] = True
    Q.append(s)
    count = 0
    while Q:
        if visited[e] == True:
            break
        
        for _ in range(len(Q)):
            q = Q.popleft()
            for n in route[q]:
                if closed[n]: continue
                if visited[n]: continue
                visited[n] = True
                previous[n] = q
                Q.append(n)

        count += 1

    return count

def remove_route(s, e):
    if s == e:
        return 
    
    tmp = previous[e]
    while tmp != s:
        closed[tmp] = True
        tmp = previous[tmp]
    

answer = 0
answer += dijkstra(S,E)
remove_route(S,E)
answer += dijkstra(E,S)
print(answer)