N, K = map(int,input().split())

dp = [[0]*(N+2) for __ in range(K+1)]

for i in range(N+2):
    dp[1][i] = 1

for i in range(2,K+1):
    for j in range(1,N+2):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K][N+1] % 1000000000)