N = int(input())
dp = [[0 for __ in range(10)] for __ in range(N)]
for i in range(10):
    dp[0][i] = 1
    
for i in range(1,N):
    for j in range(10):
        for k in range(j,10):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N-1])%10007)
