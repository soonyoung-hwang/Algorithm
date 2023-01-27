# 피보나치 수 3
# F(2k) = (F(k))^2 + 2F(k)*F(k-1)
# F(2k+1) = (F(k))^2 + (F(k-1))^2
memo = dict()
M = 1_000_000

N = int(input())


def fibonacci(N):
    # print(N)
    if N == 1:
        return 1
    elif N == 0:
        return 0
    elif N in memo:
        return memo[N]

    if N%2 == 0:
        t1 = fibonacci(N//2)
        t2 = fibonacci(N//2-1)
        memo[N] = ((t1**2) + 2*t1*t2)%M
        return memo[N]
    else:
        t1 = fibonacci((N+1)//2)
        t2 = fibonacci((N-1)//2)
        memo[N] = (t1**2 + t2**2)%M
        return memo[N]

print(fibonacci(N))