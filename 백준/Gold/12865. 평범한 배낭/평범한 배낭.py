n, k = map(int,input().split())
values = [list(map(int,input().split())) for __ in range(n)]

# dp[k] : the maximum value that we can get at that weight k
#         with the picked index of items -> 안 될듯

values.sort(reverse=True)
dp = [[-1, [1]*n] for __ in range(k+1)]
dp[0] = [0, [1]*n]

for i in range(k+1):
    for j in range(n):
        w, v = values[j]
        if i-w < 0:
            continue
        
        if dp[i-w][1][j] == 0:
            continue

        pred_flag = dp[i-w][1][:]
        if dp[i][0] < dp[i-w][0]+v:
            pred_flag[j] = 0
            dp[i] = [dp[i-w][0]+v,pred_flag]

answer = []
for i in range(k+1):
    answer.append(dp[i][0])
    
answer = max(answer)
print(answer)

