MOD = 1_000_000_000
N = int(input())

dp = [
    [[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)]
    for _ in range(N + 1)
]
for i in range(1, 10):
    dp[1][i][i][i] = 1

for n in range(2, N + 1):
    for num in range(10):
        for fr in range(10):
            for to in range(10):
                # if num != 0 and num != 9:
                if num < fr or num > to:
                    continue
                if fr == to:
                    continue
                elif num == fr:
                    dp[n][num][fr][to] = (
                        dp[n - 1][num + 1][fr][to] + dp[n - 1][num + 1][fr + 1][to]
                    ) % MOD
                elif num == to:
                    dp[n][num][fr][to] = (
                        dp[n - 1][num - 1][fr][to] + dp[n - 1][num - 1][fr][to - 1]
                    ) % MOD
                else:
                    dp[n][num][fr][to] = (
                        dp[n - 1][num + 1][fr][to] + dp[n - 1][num - 1][fr][to]
                    ) % MOD


answer = 0
for last in range(10):
    answer += dp[N][last][0][9]

print(answer % MOD)