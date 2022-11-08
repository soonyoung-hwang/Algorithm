from collections import deque
from collections import defaultdict
import sys

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for __ in range(N-1)]

routes = defaultdict(list)
for route in arr:
    routes[route[0]].append(route[1])
    routes[route[1]].append(route[0])
    
visited = [False]*(N+1)
Q = deque()
Q.append(1)

answer = [0]*(N+1)

while Q:
    node = Q.popleft()
    visited[node] = True
    
    route = routes[node]
    for i in range(len(route)):
        t = route[i]
        if not visited[t]:
            answer[t] = node
            Q.append(t)

for i in range(2,N+1):
    print(answer[i])