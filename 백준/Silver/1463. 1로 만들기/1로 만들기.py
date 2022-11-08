from collections import deque

N = int(input())
visited = [False]*(N+1)

Q = deque()
Q.append([N,0])

while Q:
    q, count = Q.popleft()
    visited[q] = True
    if q == 1:
        print(count)
        break
    
    if q%3 == 0 and not visited[q//3]:
        visited[q//3] = True
        Q.append([q//3,count+1])
    
    if q%2 == 0 and not visited[q//2]:
        visited[q//2] = True
        Q.append([q//2,count+1])
        
    if not visited[q-1]:
        visited[q-1] = True
        Q.append([q-1,count+1])
