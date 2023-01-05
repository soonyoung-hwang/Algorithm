# 1644 소수의 연속 합

import sys
input = sys.stdin.readline


# step 1 : 4,000,000 까지 모든 소수를 구해놓는다.
# step 2 : 투 포인터로 합으로 표현되는지 확인한다.

num = int(input())

# step 1
NUM = 4_000_000
arr = [True for __ in range(NUM+1)]
arr[0], arr[1] = False, False
for i in range(2,NUM):
    if arr[i]:
        for j in range(2,NUM//i+1):
            arr[i*j] = False

primes = []
for i in range(NUM):
    if arr[i]:
        primes.append(i)

# step 2
answer = 0
s, e = 0, 0
total = primes[0]
e_moved = False
while s <= len(primes)-1:
    if e < s:
        total += primes[s]
        e = s
    
    if total == num:
        answer += 1
        total -= primes[s]
        s += 1
        if total == 0:
            break
        continue

    if e+1 <= len(primes)-1 and total + primes[e+1] <= num:
        total += primes[e+1]
        e += 1
        e_moved = True
    else:
        e_moved = False
    
    if not e_moved:
        total -= primes[s]
        s += 1
        

print(answer)
