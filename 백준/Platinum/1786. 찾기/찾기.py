import sys
input = sys.stdin.readline

T = input()[:-1]
P = input()

if T[-1] == '\n':
    T = T[:-1]
if P[-1] == '\n':
    P = P[:-1]

dp = [0 for __ in range(len(P))]

def make_function():
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = dp[j-1]
        if P[i] == P[j]:
            j += 1
            dp[i] = j
        

answer = 0
answers = []
def find(T,P):
    global answer
    s = 0
    i = 0

    while s+i < len(T):
        if T[s+i] == P[i]:
            i += 1

        elif i == 0:
            s += 1
            i = 0

        else:
            next_i = dp[i-1]          # 몇 개까지 일치하는지
            s = s + i - next_i        # 일치하는 갯수만큼 뒤에서 시작
            i = next_i
        
        if i == len(P):
            answer += 1
            answers.append(s+1)

            next_i = dp[i-1]
            s = s + i-next_i 
            i = next_i

make_function()
find(T, P)
print(answer)
print(*answers)