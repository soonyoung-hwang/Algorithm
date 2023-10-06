MOD = 1_000_000_003

def find(n, k):
    if n < k:
        dp[n][k] = 0

    if dp[n][k] == -1:
        dp[n][k] = (find(n - 2, k - 1) + find(n - 1, k)) % MOD

    return dp[n][k]


N = int(input().rstrip())  # N(4 ≤ N ≤ 1,000)
K = int(input().rstrip())

dp = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = 1
    dp[i][1] = i

answer = (find(N - 3, K - 1) + find(N - 1, K)) % MOD
print(answer)
