# Parametric Search
import sys
input = sys.stdin.readline

K, N = map(int,input().split())
arr = [int(input()) for __ in range(K)]

def is_possible(num):
    res = 0
    for i in range(K):
        res += arr[i] // num
    
    if res >= N:
        return True
    
    return False

l, r = 1, 2**31
while l < r:
    m = (l+r)//2
    if is_possible(m):
        l = m+1
    else:
        r = m

print(l-1)

