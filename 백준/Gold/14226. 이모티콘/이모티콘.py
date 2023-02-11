from collections import deque
import sys
input = sys.stdin.readline

S = int(input())
visited = [[False for __ in range(2*S+1)] for __ in range(2*S+1)]
if S == 1:
    print(0)
    exit(0)

Q = deque([(1, 0)])
count = 0
visited[1][0] = True

while Q:
    for i in range(len(Q)):
        q = Q.popleft()
        if q[0] == S:
            Q = []
            break

        # action 1 : copy
        if not visited[q[0]][q[0]]:
            visited[q[0]][q[0]] = True
            Q.append((q[0],q[0]))
    
        # action 2 : paste
        if q[0]+q[1] <= 2*S and not visited[q[0]+q[1]][q[1]]:
            visited[q[0]+q[1]][q[1]] = True
            Q.append((q[0]+q[1],q[1]))
            
        # action 3 : delete
        if q[0] > 1 and not visited[q[0]-1][q[1]]:
            visited[q[0]-1][q[1]] = True
            Q.append((q[0]-1,q[1]))
    if Q:
        count += 1
            

print(count)