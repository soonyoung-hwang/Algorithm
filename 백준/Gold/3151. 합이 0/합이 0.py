# 풀이 :
#   1. 전체 경우의 수 (마이너스, 플러스, 0) 개수 : (0, 0, 3) or (2, 1, 0) or (1, 2, 0) or (1, 1, 1)
#   2. 전처리 : 모든 숫자에 대해 hash로 값이 얼마나 존재하는지 설정
#   3. 아래 경우의 수의 합을 구한다.
#       (0, 0, 3) : 0중 3개를 고르는 경우의 수 -> nC3
#       (2, 1, 0) : minus 값이 2개 이상인 경우, 모든 조합을 찾고, 그 조합의 값과 합이 0이 될 수 있는 개수를 hash에서 찾는다.
#       (1, 2, 0) : plus 도 마찬가지로 처리해준다.
#       (1, 1, 1) : (모든 minus 값과 plus값이 같은 경우) * 0의 개수 처리

from collections import defaultdict


def find():
    global answer
    A, B, C = len(minus), len(plus), len(zero)
    if C > 2:
        answer = int(C * (C - 1) * (C - 2) / 6)

    if A > 1:  # case 1 : (minus, minus, plus)
        for i in range(A):
            for j in range(i, A):
                if i == j:
                    continue
                answer += howmany[-(minus[i] + minus[j])]

    if B > 1:  # case 2 : (minus, plus, plus)
        for i in range(B):
            for j in range(i, B):
                if i == j:
                    continue
                answer += howmany[-(plus[i] + plus[j])]

    # case 3 : (minus, plus, zero)
    for i in range(1, 10001):
        answer += howmany[i] * howmany[-i] * C

    return answer


N = int(input())
codings = list(map(int, input().split()))
minus = []
plus = []
zero = []
howmany = defaultdict(int)
answer = 0
for coding in codings:
    if coding < 0:
        minus.append(coding)
    elif coding > 0:
        plus.append(coding)
    else:
        zero.append(coding)

    howmany[coding] += 1

find()
print(answer)
