# 그냥 한번 풀어보자.
import copy
from collections import deque

N, K = map(int,input().split())
MAX = max(2*K, N)
visited = [False]* (MAX+1)
visited[N] = True
Q = deque()
nextQ = deque()
Q.append(N)
count = 0


def doubling():
    # popping Q and filling nextQ
    global nextQ
    global Q
    
    nextQ = copy.deepcopy(Q)
    while Q:
        temp = Q.pop()
        if not visited[temp]:
            nextQ.appendleft(temp)
            visited[temp] = True
        
        temp *= 2
        if temp != 0 and temp < MAX and not visited[temp]:
            visited[temp] = True
            Q.appendleft(temp)
            nextQ.appendleft(temp)
    

def onestep():
    global nextQ
    global Q
    # popping nextQ and filling Q
    while nextQ:
        temp = nextQ.pop()
        if 0 <= temp-1 and not visited[temp-1]:
            visited[temp-1] = True
            Q.appendleft(temp-1)
        
        if temp+1 <= MAX and not visited[temp+1]:
            visited[temp+1] = True
            Q.appendleft(temp+1)
                
doubling()
# Q 비어있고 nextQ 만 있어
while visited[K] == False:
    count += 1
    onestep()
    # nextQ 비어있고 Q만 있어
    doubling()
    # Q 비어있고 nextQ만 남게 됨
    
    
print(count)