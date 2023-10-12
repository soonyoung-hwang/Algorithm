# 2차원 dp면 될거 같다.
T, W = map(int, input().rstrip().split())
drops = [int(input()) for _ in range(T)]

# dp[m][t][loc] : m 번째 움직였을 때, t번째에 loc 인덱스의 열매를 먹었을 때, 얻을 수 있는 최대 값
dp = [[[0 for _ in range(2)] for _ in range(T + 2)] for _ in range(W + 1)]
for m in range(0, W + 1):
    for t in range(T - 1, -1, -1):
        if drops[t] == 1:
            if m == 0:
                dp[m][t][0] = dp[m][t + 1][0] + 1
                dp[m][t][1] = dp[m][t + 1][1]
                continue

            dp[m][t][0] = max(
                dp[m][t + 1][0] + 1,
                dp[m - 1][t + 1][1] + 1,
                # dp[m - 1][t + 1][0] + 1,
            )
            dp[m][t][1] = max(dp[m][t + 1][1], dp[m - 1][t + 1][1])

        elif drops[t] == 2:
            if m == 0:
                dp[m][t][0] = dp[m][t + 1][0]
                dp[m][t][1] = dp[m][t + 1][1] + 1
                continue

            dp[m][t][1] = max(
                dp[m][t + 1][1] + 1,
                dp[m - 1][t + 1][0] + 1,
                # dp[m - 1][t + 1][1] + 1,
            )
            dp[m][t][0] = max(dp[m][t + 1][0], dp[m - 1][t + 1][0])


print(max(dp[W][0][0], dp[W - 1][0][1]))