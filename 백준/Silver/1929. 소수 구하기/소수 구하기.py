def is_prime(n):
    if n == 1:
        return False
    ret = True
    k = int(n**(1/2))+1
    for i in range(2,k):
        if n % i == 0:
            ret = False
            break
    return ret

N,M = map(int,input().split())
for i in range(N,M+1):
    if is_prime(i):
        print(i)