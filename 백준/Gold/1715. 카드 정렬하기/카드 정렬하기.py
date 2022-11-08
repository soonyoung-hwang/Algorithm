import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for __ in range(N)]
heapq.heapify(arr)
stack = []
answer = 0

for i in range(N-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    c = a + b
    answer += c
    heapq.heappush(arr,c)

print(answer)
