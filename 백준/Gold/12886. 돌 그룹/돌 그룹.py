from collections import defaultdict

def mix(a, b):
    if a == b:
        return a, b
    elif a > b:
        return a - b, 2 * b
    else:
        return a * 2, b - a


A, B, C = map(int, input().split())
visited = defaultdict(bool)

Q = [(A, B, C)]
answer = 0
while Q:
    a, b, c = Q.pop()

    if a == b and b == c:
        answer = 1
        break

    visited[(a, b, c)] = True

    # a, b
    na, nb = mix(a, b)
    if not visited[(na, nb, c)]:
        Q.append((na, nb, c))
        visited[(na, nb, c)] = True

    # b, c
    nb, nc = mix(b, c)
    if not visited[(a, nb, nc)]:
        Q.append((a, nb, nc))
        visited[(a, nb, nc)] = True

    # a, c
    na, nc = mix(a, c)
    if not visited[(na, b, nc)]:
        Q.append((na, b, nc))
        visited[(na, b, nc)] = True

print(answer)
