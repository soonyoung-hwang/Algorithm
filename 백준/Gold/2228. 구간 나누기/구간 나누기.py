def find_max(i, j):
    temp_max = numbers[i]
    temp_sum = numbers[i]

    for number in numbers[i + 1 : j + 1]:
        if temp_sum < 0:
            if temp_sum < number:
                temp_sum = number
        elif temp_sum + number < 0:
            temp_sum = 0  # 모두 뺀다.

        else:
            temp_sum += number

        temp_max = max(temp_max, temp_sum)

    return temp_max


N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

# dp[i][j][k] : i 개의 구간으로 나누어져있을 때, i번째 숫자부터 j번째 숫자까지의 최대값
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(M + 1)]

# M = 1일 때 직접 구한다.
for i in range(N):
    for j in range(i, N):
        dp[1][i][j] = find_max(i, j)


# 나머지는 dp로 구해준다.
for m in range(2, M + 1):
    for i in range(N):
        for j in range(i, N):
            temp_max = -33000 * 50

            for dif in range(j - i - 1):
                if dp[1][i][i + dif] == -33000 or dp[m - 1][i + dif + 2][j] == -33000:
                    continue
                temp_max = max(temp_max, dp[1][i][i + dif] + dp[m - 1][i + dif + 2][j])

            dp[m][i][j] = temp_max

print(dp[M][0][N - 1])