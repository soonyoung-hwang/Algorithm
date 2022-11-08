import heapq
import sys

N, k = map(int,input().split())
gems = []
bags = []
possibles = []
for _ in range(N):
    gems.append(list(map(int, sys.stdin.readline().split())))

for _ in range(k):
    bags.append(int(input()))

gems.sort(reverse=True)
bags.sort()
answer = 0

for i in range(k):
    while(gems and gems[-1][0] <= bags[i]):
        gem = gems.pop()
        heapq.heappush(possibles,-gem[1])
    
    if(possibles):
        put_in = heapq.heappop(possibles)
        answer += -put_in

print(answer)