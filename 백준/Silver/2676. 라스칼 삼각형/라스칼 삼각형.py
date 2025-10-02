import sys

input = sys.stdin.readline

T = []
N = int(input().strip())
for i in range(N):
    T.append(list(map(int, input().split())))


for test_case in T:
    m, n = test_case[0], test_case[1]

    if n > m // 2:
        n = m - n

    ans = 1
    for i in range(n):
        ans += (m - 1) - 2 * i

    print(ans)