import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

answer = 0

for i in range(N):
    l, r = 0, N-1

    target = arr[i]
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        if arr[l]+arr[r] == target:
            answer += 1
            break
        elif arr[l]+arr[r] > target:
            r -= 1
        else:
            l += 1

print(answer)
