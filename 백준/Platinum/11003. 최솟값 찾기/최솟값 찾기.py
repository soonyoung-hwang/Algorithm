# 최솟값 찾기
from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int,input().split())
arr = list(map(int,input().split()))

answer = []
Q = deque()

for i in range(L):
    while Q and Q[-1][0] >= arr[i]:
        Q.pop()
    
    Q.append((arr[i], i))
    answer.append(Q[0][0])

for i in range(L,N):
    while Q and Q[-1][0] >= arr[i]:
        Q.pop()
    
    Q.append((arr[i], i))
    if Q[0][1] == (i-L):
        Q.popleft()
    
    answer.append(Q[0][0])

print(*answer)