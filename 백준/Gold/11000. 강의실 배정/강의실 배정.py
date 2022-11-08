import sys
import heapq

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()
ans = []

for i in range(N):
    if(len(ans)== 0):
        heapq.heappush(ans,[arr[i][1],arr[i][0]])
        continue
    
    if(ans[0][0] <= arr[i][0]):
        k = heapq.heappop(ans)
        k[0] = arr[i][1]
        heapq.heappush(ans,k)

    else:
        heapq.heappush(ans,[arr[i][1],arr[i][0]])    
    
print(len(ans))