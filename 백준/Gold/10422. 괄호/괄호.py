MOD = 1_000_000_007
dp = [0 for _ in range(5001)]
dp[0] = 1
dp[2] = 1
for i in range(4, 5001, 2):
    temp = 0
    for j in range(0, i, 2):
        temp += (dp[j] * dp[i - j - 2]) % MOD
    dp[i] = temp % MOD

T = int(input())
for _ in range(T):
    print(dp[int(input().rstrip())])
