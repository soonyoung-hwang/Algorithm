dp = [[0, 0] for __ in range(41)]
# dp[i] = dp[i-1] + dp[i-2]
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,41):
    dp[i][0] = dp[i-1][0]+dp[i-2][0]
    dp[i][1] = dp[i-1][1]+dp[i-2][1]

t = int(input())
ns = []
for __ in range(t):
    ns.append(int(input()))

for i in range(t):
    n = ns[i]
    print(*dp[n],sep=' ')