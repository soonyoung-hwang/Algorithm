N = int(input())
k = int(input())
arr = list(map(int,input().split()))

arr.sort()
if(len(arr) == 1 or N <= k):
    print(0)

else:
    answer = arr[-1]-arr[0]
    temp = []
    for i in range(N-1):
        temp.append(arr[i+1]-arr[i])

    temp.sort(reverse=True)
    for i in range(k-1):
        answer -= temp[i]

    print(answer)