# 평범한 배낭 (Knapsack Problem)

N, K = map(int,input().split())
arr = [list(map(int,input().split())) for __ in range(N)]


dp = [[0 for __ in range(K+1)] for __ in range(N+1)]
arr.sort(reverse=True)
for i in range(1,N+1):
    # i = 1
    for j in range(1,K+1):
        dp[i][j] = dp[i-1][j]
        if j-arr[i-1][0] >= 0:  # 이번 줄에서 arr를 담을 수 있는 경우
            dp[i][j] = max(dp[i][j], dp[i-1][j-arr[i-1][0]]+arr[i-1][1])
        

print(dp[N][K])