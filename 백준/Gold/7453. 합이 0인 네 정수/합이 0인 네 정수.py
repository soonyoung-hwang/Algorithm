# part 1 : (A, B), (C, D) 로 나오는 모든 경우의 수 구하기
# part 2 : (A, B), (C, D) 조합 정렬 => AB // CD
# part 3 : AB // CD 를 two pointer로 합이 0 되는 구간 찾기

# 실행속도 계산
# part 1 : 16000000 * 2 => 약 3200만
# part 2 : [16000000 * log(16000000)] * 2 => 약 8억
# part 3 : 32000000 => 약 3200만
# total : 약 8억 -> 8초 -> 통과

import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for __ in range(N):
    a, b, c, d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# part 1
AB = [a+b for a in A for b in B]
CD = [c+d for c in C for d in D]

# part 2
AB.sort()
CD.sort()

# part 3
i, j = 0, N*N-1
answer = 0
while i < N*N and j >= 0:
    t = AB[i] + CD[j]
    if t == 0:
        aa = 1
        bb = 1

        while i < N*N-1 and AB[i]==AB[i+1]: # 다음 i가 현재 i와 다를 때까지 세준다.
            i += 1
            aa += 1

        while j > 0 and CD[j] == CD[j-1]:   # 다음 j가 현재 j와 다를 때까지 세준다.
            j -= 1
            bb += 1

        answer += aa * bb   # 정답에 모든 경우의 수 더해준다.

        if i < N*N-1:
            i += 1
            continue
        if j > 0:
            j -= 1
            continue
        
        break

    if t > 0:
        j -= 1
    
    else:
        i += 1

print(answer)