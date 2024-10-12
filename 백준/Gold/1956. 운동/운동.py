import sys
input = sys.stdin.readline
MAX = sys.maxsize

V, E = map(int, input().split())
route = [[MAX for _ in range(V + 1)] for _ in range(V + 1)]
for i in range(E):
    a, b, c = map(int, input().split())
    route[a][b] = c

for mid in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            route[i][j] = min(route[i][j], route[i][mid] + route[mid][j])

answer = MAX
for i in range(1, V + 1):
    answer = min(answer, route[i][i])

print(answer if answer != MAX else -1)
