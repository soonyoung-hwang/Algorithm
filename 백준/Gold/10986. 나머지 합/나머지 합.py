import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))
left_num = [0 for __ in range(M)]

# 전처리
new_arr = [arr[0]%M]
for i in range(1, N):
    new_arr.append((new_arr[-1]+arr[i])%M)

for i in range(N):
    left_num[new_arr[i]] += 1

# 메인 알고리즘
answer = 0
need = 0
for i in range(N):
    answer += left_num[need]
    left_num[new_arr[i]%M] -= 1
    need = (need+arr[i])%M
    

print(answer)