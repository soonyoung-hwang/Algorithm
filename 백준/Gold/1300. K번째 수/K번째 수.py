N = int(input())
k = int(input())

def find_index(num):
    # got num and return 그 숫자의 max index
    tmp = 0
    for i in range(1,N+1):
        tmp += min(num//i, N)
    
    return tmp


l,r = 0, N*N
while l < r:
    mid = (l+r)//2
    if find_index(mid) >= k:
        r = mid
    else:
        l = mid+1

answer = r
print(answer)
