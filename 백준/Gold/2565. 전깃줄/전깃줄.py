def find_lowerbound(v, arr):
    l,r = 0, len(arr)-1
    while l < r:
        mid = (l+r)//2
        if arr[mid] > v:
            r = mid
        else:
            l = mid+1

    return l


def LIS(arr):
    temp = []
    for v in arr:
        if not temp:
            temp.append(v)
            continue
        
        if temp[-1] < v:
            temp.append(v)
            continue
        
        idx = find_lowerbound(v,temp)
        temp[idx] = v
    
    return len(temp)

n = int(input())
arr = [list(map(int,input().split())) for __ in range(n)]

arr.sort()
for i in range(n):
    arr[i] = arr[i][1]
    
print(n - LIS(arr))
