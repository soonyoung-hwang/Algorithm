# 수 묶기
# 1. 묶는 수가 클 수록 좋은 효과가 나는 것 / 2 이상의 양수
# 2. 묶는 수가 작을수록 좋은 효과가 나는 것 / 0 포함 음수
# 3. 무조건 안 묶으면 좋은 효과가 나는 것 -> 1의 집합
# 로 array를 구성해서 가장 좋은 효과가 나도록 sort 해 준 다음에 앞에 수 부터 묶어 계산해준다.


N = int(input())
plus_arr = []
minu_arr = []
one_arr = []

for __ in range(N):
    num = int(input())
    if num <= 0:
        minu_arr.append(num)
    elif num == 1:
        one_arr.append(num)
    else:
        plus_arr.append(num)

plus_arr.sort(reverse=True)
minu_arr.sort()

answer = 0
for i in range(len(plus_arr)//2):
    answer += plus_arr[i*2]*plus_arr[i*2+1]

if(len(plus_arr)%2):
    answer += plus_arr[-1]

for i in range(len(minu_arr)//2):
    answer += minu_arr[i*2]*minu_arr[i*2+1]

if(len(minu_arr)%2):
    answer += minu_arr[-1]

answer += len(one_arr)
print(answer)