# 백준 2170 : 선 긋기
# 풀이 :
#   1. 입력받은 숫자들을 모두 정렬한다 (NlogN)
#   2. 정렬된 숫자를 기준으로 앞에서 부터 stack에 넣어준다.
#       만약 앞에 수와 뒤에 수가 겹친다면, 합쳐준다
#       안 겹친다면, 새로 넣어준다.
#   3. stack의 모든 range로 부터 길이를 구한다.


import sys

input = sys.stdin.readline
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

numbers.sort()
stack = []
for number in numbers:
    if not stack:
        stack.append(number[:])
        continue

    if stack[-1][1] >= number[0]:
        stack[-1][1] = max(stack[-1][1],number[1])

    else:
        stack.append(number[:])


answer = 0
for number in stack:
    answer += number[1] - number[0]

print(answer)
