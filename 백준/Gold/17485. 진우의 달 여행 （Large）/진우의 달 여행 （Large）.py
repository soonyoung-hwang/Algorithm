import sys

input = sys.stdin.readline

N, M = map(int, input().split())
box = []
for _ in range(N):
    box.append(tuple(map(int, input().split())))

MAX_VALUE = 1000 * 100 + 1
dp = [[[1000 * 100 + 1 for _ in range(3)] for _ in range(M)] for _ in range(N + 1)]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = 0

for r in range(N):
    for c in range(M):
        if c - 1 >= 0:
            dp[r + 1][c][0] = box[r][c - 1] + min(dp[r][c - 1][1], dp[r][c - 1][2])
        if c + 1 < M:
            dp[r + 1][c][2] = box[r][c + 1] + min(dp[r][c + 1][0], dp[r][c + 1][1])
        dp[r + 1][c][1] = box[r][c] + min(dp[r][c][0], dp[r][c][2])


answer = 1000 * 100 + 1
for i in range(M):
    answer = min(answer, min(dp[N][i]))

print(answer)
