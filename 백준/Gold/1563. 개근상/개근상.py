MOD = 1_000_000

N = int(input())
dp = [[[0 for _ in range(3)] for _ in range(N + 1)] for _ in range(2)]
dp[0][1][0] = 1
dp[0][1][1] = 1
dp[0][1][2] = 0
dp[1][1][0] = 1
dp[1][1][1] = 0
dp[1][1][2] = 0

for i in range(2, N + 1):
    dp[0][i][0] = sum(dp[0][i - 1]) % MOD  # 이번거가 O
    dp[0][i][1] = dp[0][i - 1][0]  # A
    dp[0][i][2] = dp[0][i - 1][1]  # A

    dp[1][i][0] = (sum(dp[0][i - 1]) + sum(dp[1][i - 1])) % MOD  # 이번거가 L  # 이번거가 O
    dp[1][i][1] = dp[1][i - 1][0]  # A
    dp[1][i][2] = dp[1][i - 1][1]  # A

print((sum(dp[0][N]) + sum(dp[1][N])) % MOD)