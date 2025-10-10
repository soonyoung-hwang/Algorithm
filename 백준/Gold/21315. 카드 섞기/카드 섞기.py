from collections import deque

N = int(input())
cards = list(map(int, input().split()))


def nanum(ret, k):
    last = N - 1
    ret1 = [ret[last]]
    for i in range(1, k + 1):
        ret1.extend(ret[last - 2 ** (i - 1) : last])
        last -= 2 ** (i - 1)

    ret1.extend(ret[0 : N - 2**k])
    return ret1


answer = []
for i in range(1, 10):
    for j in range(1, 10):
        if 2**i > N or 2**j > N:
            continue

        ret = [i for i in range(1, N + 1)]
        if nanum(nanum(ret, i), j) == cards:
            answer = [i, j]
            break

    if answer:
        break

print(*answer)