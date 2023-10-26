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