import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

Q = []
for a in A:
    if not Q:
        Q.append(a)
        continue

    if Q[-1] < a:
        Q.append(a)
        continue

    idx = bisect_left(Q,a)
    Q[idx] = a
    
print(len(Q))