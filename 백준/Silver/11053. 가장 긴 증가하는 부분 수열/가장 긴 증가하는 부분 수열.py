def find_location(arr,v):
    # find the index that is just bigger than 'v'
    # example : arr = [10, 20, 30, 60], v = 25, we need to return 2 
    # because the value at 2nd index is just bigger than or equal to 25
    
    if not arr:
        return 0
    
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] < v:
            l = m+1
        else:
            r = m-1
    
    return l

N = int(input())
nums = list(map(int,input().split()))

arr = []

for num in nums:
    if not arr:
        arr.append(num)
        continue
    
    i = find_location(arr, num)
    if i == len(arr):
        arr.append(num)
    else:
        arr[i] = num

print(len(arr))