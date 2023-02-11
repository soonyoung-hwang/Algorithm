import heapq
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
before = [0 for __ in range(N+1)]
after = [[] for __ in range(N+1)]
for __ in range(M):
    a, b = map(int,input().split())
    after[a].append(b)
    before[b] += 1

answer = []

Q = []
for i in range(1,N+1):
    if before[i] == 0:
        Q.append(i)

heapq.heapify(Q)
while Q:
    q = heapq.heappop(Q)
    answer.append(q)
    for n in after[q]:
        before[n] -= 1
        if before[n] == 0:
            heapq.heappush(Q,n)
    
print(*answer)