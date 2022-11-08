N = int(input())
houses = []
for __ in range(N):
    houses.append(list(map(int,input().split())))

dp = [[1e6 for __ in range(3)] for __ in range(N+1)]
for i in range(3):
    dp[0][i] = 0
    
for i in range(1,N+1):
    for j in range(3):
        for k in range(3):
            if k != j:
                dp[i][j] = min(dp[i][j],dp[i-1][k]+houses[i-1][j])
        
print(min(dp[N]))
