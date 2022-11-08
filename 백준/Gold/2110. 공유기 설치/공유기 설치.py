import sys
input = sys.stdin.readline

def num_need(m,N):
    distance = 0
    count = 1
    for i in range(N-1):
        distance += arr[i+1]-arr[i]
        if distance >= m:
            count += 1
            distance = 0
    
    return count



N, C = map(int,input().split())
arr = [int(input()) for __ in range(N)]
arr.sort()


l, r = 0, 1000000000
    
while l < r:
    m = (l+r)//2
    if num_need(m,N) >= C:
        l = m+1
    else:
        r = m

answer = l-1
print(answer)


    