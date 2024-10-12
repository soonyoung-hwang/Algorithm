import sys
from collections import deque

input = sys.stdin.readline

dd = ((0, 1), (0, -1), (1, 0), (-1, 0))

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

cnt = 0
# init
Q = deque([])
for i in range(N):
    arr[i][0] = 9
    arr[i][-1] = 9
    Q.append((i, 0))
    Q.append((i, M - 1))

for i in range(M):
    arr[0][i] = 9
    arr[-1][i] = 9
    Q.append((0, i))
    Q.append((N - 1, i))

cnt = N * 2 + M * 2 - 4

while Q:
    r, c = Q.popleft()
    for i in range(4):
        nr, nc = r + dd[i][0], c + dd[i][1]
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if arr[nr][nc] == 9 or arr[nr][nc] == 1:
            continue
        arr[nr][nc] = 9
        cnt += 1
        Q.append((nr, nc))

cheeses = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheeses.add((i, j))

time_count = 0
while cnt < N * M:
    # remove cheese
    to_remove = set()
    for cheese in cheeses:
        r, c = cheese
        air_cnt = 0
        for i in range(4):
            nr, nc = r + dd[i][0], c + dd[i][1]
            if arr[nr][nc] == 9:
                air_cnt += 1

        if air_cnt >= 2:
            to_remove.add((r, c))

    cnt += len(to_remove)
    for cheese in to_remove:
        r, c = cheese
        arr[r][c] = 9

    cheeses = cheeses - to_remove

    # udpate outside air
    Q = deque(to_remove)
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dd[i][0], c + dd[i][1]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nr][nc] == 9 or arr[nr][nc] == 1:
                continue
            arr[nr][nc] = 9
            cnt += 1
            Q.append((nr, nc))

    time_count += 1

print(time_count)
