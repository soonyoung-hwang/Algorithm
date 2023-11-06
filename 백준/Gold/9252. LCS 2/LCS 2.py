A = input().rstrip()
B = input().rstrip()

dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
up = [[False for _ in range(len(A)+1)] for _ in range(len(B)+1)]

# dp 찾기
# dp[i][j] = dp[i-1][j-1] + 1             (if B[i] == A[j])
#          = max(dp[i-1][j], dp[i][j-1])  (else)
for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if A[j-1] == B[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
            up[i][j] = True
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = []

# dp에서 수열 찾기
next_value = dp[len(B)][len(A)]
to = len(A)
for i in range(len(B), 0, -1):
    for j in range(1, to+1):
        if dp[i][j] == next_value and up[i][j]:
            answer.append(A[j-1])
            next_value -= 1
            to = j-1
            break

print(len(answer))
print(''.join(answer[::-1]))