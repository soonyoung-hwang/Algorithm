import sys

input = sys.stdin.readline

N = int(input().strip())
sums = []
for i in range(N):
    sums.append(int(input()))

total = sum(sums) // 2

for i in range(N):
    temp = 0
    for j in range(i + 1, i + N, 2):
        temp += sums[(j % N)]

    print(total - temp)
