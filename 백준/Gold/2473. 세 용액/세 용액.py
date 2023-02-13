import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

found = False
best = 3000000001
for i in range(N-2):
    if found: break
    base = arr[i]
    start, end = i+1, N-1
    while start < end:
        tmp = base+arr[start]+arr[end]
        if abs(tmp) < best:
            best = abs(tmp)
            answer = [base, arr[start], arr[end]]
        
        if tmp == 0:
            found = True
            break
        elif tmp > 0:
            end -= 1
        else:
            start += 1
    
print(*answer)