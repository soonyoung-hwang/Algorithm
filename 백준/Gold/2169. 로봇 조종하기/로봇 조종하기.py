from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, M):
    arr[0][i] = arr[0][i] + arr[0][i - 1]

for i in range(1, N):
    left = deque([arr[i][0] + arr[i - 1][0]])
    right = deque([arr[i][M - 1] + arr[i - 1][M - 1]])
    for j in range(1, M):
        _next = max(left[-1], arr[i - 1][j]) + arr[i][j]
        left.append(_next)

    for j in range(M - 2, -1, -1):
        _next = max(right[0], arr[i - 1][j]) + arr[i][j]
        right.appendleft(_next)

    for j in range(M):
        arr[i][j] = max(left[j], right[j])

print(arr[N - 1][M - 1])
