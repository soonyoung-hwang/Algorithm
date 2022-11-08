from bisect import bisect_right
import sys
input = sys.stdin.readline
# some number = a + b 라고 하면,  a, b 둘 중 하나는 some number 의 절반보다 작거나 같다.
# 따라서 some number 의 절반의 prime 만 구한 다음에 찾아주면 된다.

T = int(input())
ns = []
for __ in range(T):
    ns.append(int(input()))
    
def is_prime(num):
    flag = True
    if num == 2:
        return True
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            flag = False
            break
    
    return flag
    
to_find = max(ns)/2

primes = []
for i in range(2, int(to_find)+1):
    if is_prime(i):
        primes.append(i)


for n in ns:
    s = bisect_right(primes,n/2)-1
    while s >= 0:
        if is_prime(n-primes[s]):
            print(primes[s], n-primes[s])
            break
        s -= 1
