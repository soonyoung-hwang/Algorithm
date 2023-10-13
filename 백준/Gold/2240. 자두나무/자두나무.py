T, W = map(int, input().split())
drops = [int(input()) for _ in range(T)]


dp = [[0 for _ in range(T + 1)] for _ in range(2)]
for moving in range(W + 1):
    for t in range(1, T + 1):
        if moving % 2 == 0:
            if drops[t - 1] == 1:
                dp[0][t] = max(dp[0][t - 1] + 1, dp[1][t - 1] + 1)
            else:
                dp[0][t] = dp[0][t - 1]

        else:
            if drops[t - 1] == 2:
                dp[1][t] = max(dp[1][t - 1] + 1, dp[0][t - 1] + 1)
            else:
                dp[1][t] = dp[1][t - 1]

print(max(dp[0][T], dp[1][T]))