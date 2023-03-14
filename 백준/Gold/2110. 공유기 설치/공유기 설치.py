import sys
input = sys.stdin.readline

N, C = map(int,input().split())
houses = [int(input()) for __ in range(N)]


def max_num(gap): # return maximum number of 공유기 if 최대 거리가 k
    res = 1
    start = houses[0]
    for i in range(1,N):
        if houses[i] >= start+gap:
            res += 1
            start = houses[i]
    
    return res
        
    
houses.sort()
l, r = 0, 1_000_000_001

while l < r:
    mid = (l+r)//2
    if max_num(mid) >= C:
        l = mid+1
    else:
        r = mid

print(l-1)