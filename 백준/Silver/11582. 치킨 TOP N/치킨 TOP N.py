N = int(input())
arr = list(map(int,input().split()))
k = int(input())

m = int(N/k)

answer = []
for i in range(0,N,m):
    answer.extend(sorted(arr[i:i+m]))

print(*answer)


