# 결국 소수의 제곱으로 나눠지면 끝이다. 2, 3, 5, 7, 11 ,... 소수 < 1,000,000 의 제곱만 검사해서 빼주면 된다.
# 10^6개에서 소수는 훨씬 적다. 솔직히 시간 복잡도 계산은 힘들고(소수의 갯수가 얼마나 나올지 시간복잡도로 계산이 힘들다 )
# 어쨋든 10^6이 에서 꽤 압축이 될 것이다. 계산 결과 약 80000개 있다. 여전히 10^6 * 80000 너무 높다.
# 따라서 소수별로 제곱해서 min ~ max 사이에 그 제곱한 수의 배수를 모두 제거해준다. (모든 수를 1로 초기화 한 후 해당 수를 0으로 만든다)
# memory에서 1인 것들은 ㄴㄴ 제곱수이다.

min_, max_ = map(int,input().split())

primes = []
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

for i in range(2,int(max_**(1/2))+2):
    if is_prime(i):
        primes.append(i)

mem = [1 for __ in range(max_-min_+1)]
for i in range(len(primes)):
    k = primes[i]**2
    if (min_)%k == 0:
        mem[0] = 0
    
    start = k - (min_ % k)
    while start <= max_-min_:
        mem[start] = 0
        start += k

print(sum(mem))