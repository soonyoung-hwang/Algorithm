# 가장 긴 증가하는 부분수열4
# 앞선 가장 긴 증가하는 부분수열과 뭐가 다른지 모르겠다..
# 수열을 출력해야 해서 더 어려운거 같은데 별 4개밖에 안되네..?


# stack 을 이용한 풀이 인데, 설명을 글로쓰기가 어렵다...ㅠ
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