def pr_search(arr, value):
    # return index of value in arr
    l, r = 0, len(arr)-1
    while l < r:
        m = (l+r)//2
        if arr[m] < value:
            l = m+1
        elif arr[m] > value:
            r = m
        else:
            l = m
            break

    return l
            
dp = [0]
c = 1
q = 0
while dp[-1] < 2**31+1:
    if c % 2 == 1:
        add = c//2+1
    else:
        add = c//2
    dp.append(dp[-1] + add)
    c += 1

t = int(input())
distances = []
for __ in range(t):
    x, y = map(int,input().split())
    distances.append(y-x)
    

for i in range(t):
    print(pr_search(dp,distances[i]))

