import sys

T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

As = []
Bs = []
for i in range(N):
    tmp = A[i]
    As.append(tmp)
    for j in range(i+1,N):
        As.append(tmp+A[j])
        tmp = tmp+A[j]

for i in range(M):
    tmp = B[i]
    Bs.append(tmp)
    for j in range(i+1,M):
        Bs.append(tmp+B[j])
        tmp = tmp+B[j]

As.sort()
Bs.sort(reverse=True)

answer = 0
start_A, start_B = 0, 0

while start_A < len(As) and start_B < len(Bs):
    tmp = As[start_A] + Bs[start_B]
    if tmp < T:
        start_A += 1
    elif tmp > T:
        start_B += 1
    else:
        count_A = 1
        count_B = 1
        
        while start_A < len(As)-1:
            if As[start_A] != As[start_A+1]:
                break
            start_A += 1
            count_A += 1
        
        while start_B < len(Bs)-1:
            if Bs[start_B] != Bs[start_B+1]:
                break
            start_B += 1
            count_B += 1
        
        answer += count_A*count_B
        start_A += 1

print(answer)