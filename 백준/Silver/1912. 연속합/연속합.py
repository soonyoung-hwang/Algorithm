N = int(input())
arr = list(map(int,input().split()))

dp = [[arr[0],arr[0]]]
for i in range(1,N):
    ndp_0 = max(dp[i-1][0], dp[i-1][1])
    ndp_1 = max(dp[i-1][1]+arr[i], arr[i])
    ndp = [ndp_0, ndp_1]
    dp.append(ndp)

print(max(dp[N-1]))