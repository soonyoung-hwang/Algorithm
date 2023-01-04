import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for __ in range(N)]

dp = [0 for __ in range(N+1)]

for i in range(N-1,-1,-1):
    if i+arr[i][0]<= N:
        dp[i]= dp[i+arr[i][0]] + arr[i][1]

    dp[i] = max(dp[i], dp[i+1])

print(dp[0])