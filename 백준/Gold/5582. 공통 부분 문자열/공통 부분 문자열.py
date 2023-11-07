from collections import deque

A = input().rstrip()
B = input().rstrip()

if len(A) > len(B):
    A, B = B, A

C = deque(B)
comparison = deque()
answer = 0
while C:
    comparison.appendleft(C.pop())
    if len(comparison) > len(A):
        comparison.pop()
    cnt = 0
    for i in range(len(comparison)):
        if comparison[i] == A[i]:
            cnt += 1
        else:
            answer = max(answer,cnt)
            cnt = 0
    else:
        answer = max(answer,cnt)

while comparison:
    comparison.pop()
    cnt = 0
    for i in range(0, len(comparison)):
        if comparison[-(i+1)] == A[-(i+1)]:
            cnt += 1
        else:
            answer = max(answer,cnt)
            cnt = 0
    else:
        answer = max(answer,cnt)

print(answer)