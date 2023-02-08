# 백준 이항계수 3
# 참고 : https://rhdtka21.tistory.com/123
# 카르마의 소정리 nCk = N!%p * (K!(N-K)!)^(p-2)%p
# 카르마의 소정리를 모른다면 풀 수 없던 문제였다.

MODULAR = 1_000_000_007

N, K = map(int,input().split())
K = N-K if K > N//2 else K

dp = [1]
# find factorial
for i in range(1,N+1):
    dp.append(dp[-1]*i % MODULAR)


def power(num, n):
    if n == 2:
        return num**2
    elif n == 1:
        return num
    elif n%2 == 0:
        return (power(num, n//2)**2) % MODULAR
    else:
        return (power(num, n//2)**2 * num) % MODULAR

answer = (dp[N]%MODULAR) * (power(dp[K]*dp[N-K], MODULAR-2)%MODULAR)
print(answer%MODULAR)