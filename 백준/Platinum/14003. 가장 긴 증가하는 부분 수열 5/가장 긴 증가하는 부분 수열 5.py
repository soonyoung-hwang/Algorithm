from bisect import bisect_left

N = int(input())
arr = list(map(int,input().split()))

stack = []
loc = [-1 for __ in range(N)]

for i in range(N):
    if not stack:
        stack.append(arr[i])
        loc[i] = 1
        continue

    if arr[i] > stack[-1]:
        stack.append(arr[i])
        loc[i] = len(stack)
        continue

    next_loc = bisect_left(stack, arr[i])
    stack[next_loc] = arr[i]
    loc[i] = next_loc+1

answer = []
top = max(loc)
for i in range(N-1,-1,-1):
    if loc[i] == top:
        answer.append(arr[i])
        top -= 1

answer.reverse()
print(len(answer))
print(*answer)