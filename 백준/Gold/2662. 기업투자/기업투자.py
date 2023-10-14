N, M = map(int, input().split())
invests = [[0 for _ in range(M + 1)]]
for _ in range(N):
    invests.append(list(map(int, input().split())))

dp = [[[0 for _ in range(M + 1)] for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, M + 1):
    for j in range(0, N + 1):
        # update dp[j][i]
        temp_max = 0
        for k in range(0, j + 1):
            candi = dp[k][i - 1][0] + invests[j - k][i]
            if candi > temp_max:
                temp_max = candi

                dp[j][i][0] = candi
                for l in range(1, i):
                    dp[j][i][l] = dp[k][i - 1][l]

                dp[j][i][i] = j - k

answer = [0 for _ in range(M + 1)]
temp_max = 0
for i in range(1, N + 1):
    if dp[i][M][0] > temp_max:
        temp_max = dp[i][M][0]
        answer = dp[i][M][:]

print(answer[0])
print(*answer[1:])
