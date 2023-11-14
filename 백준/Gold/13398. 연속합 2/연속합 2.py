N = int(input())
arr = list(map(int,input().split()))

# ec1 : 모두 마이너스 -> 한 수만 선택

current = 0
dp = [[0 for _ in range(N+1)] for _ in range(2)]

for i in range(1, N+1):
    if arr[i-1] < 0:
        if dp[0][i-1] + arr[i-1] > 0:
            dp[0][i] = dp[0][i-1] + arr[i-1]
        else:
            dp[0][i] = 0

        dp[1][i] = max(dp[0][i-1], dp[1][i-1]+arr[i-1])

    else:
        dp[0][i] = dp[0][i-1] + arr[i-1]
        dp[1][i] = dp[1][i-1] + arr[i-1]

answer = max(max(dp[0]), max(dp[1]))
if max(arr) < 0:
    answer = max(arr)
print(answer)
