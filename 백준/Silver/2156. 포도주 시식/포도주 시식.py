import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp = [[0 for __ in range(3)] for __ in range(n)]
dp[0][1] = arr[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]
    # print(i, arr[i], dp[i])
print(max(dp[n-1]))