from collections import defaultdict

N, P, Q = map(int,input().split())
dp = defaultdict(int)
dp[0] = 1

def A(num):
    if dp[num] != 0:
        return dp[num]
    dp[num] = A(num//P) + A(num//Q)
    return dp[num]


print(A(N))