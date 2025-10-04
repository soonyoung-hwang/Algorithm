# 벽 부수고 이동하기 4
# 어차피 부술 수 있는 벽은 최대 1개
# 0으로 이동할 수 있는 곳들을 모두 색을 칠해놓고
# 그 벽을 부셨을 때, 상하좌우 갔을 때, 해당 색들의 합을 구하면 된다.


# 1000 X 1000
# 1000 X 1000 X 4

from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
box = []
for _ in range(N):
    T = input().rstrip()
    box.append([int(T[i]) for i in range(M)])

dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
color_count = defaultdict(int)


def dfs(r, c, color):
    # color 색칠 및 color 별 총합 개수
    box[r][c] = color
    color_count[color] += 1
    for i in range(4):
        nr, nc = r + dd[i][0], c + dd[i][1]
        if nr < 0 or nc < 0 or nr > N - 1 or nc > M - 1:
            continue
        if box[nr][nc]:
            continue

        dfs(nr, nc, color)


color = 2  # color starts from 2

for i in range(N):
    for j in range(M):
        if box[i][j]:
            continue
        dfs(i, j, color)
        color += 1

answer = [[0 for _ in range(M)] for _ in range(N)]

for r in range(N):
    for c in range(M):
        if box[r][c] != 1:
            continue

        cnt = 1
        color_near = set()
        for i in range(4):
            nr, nc = r + dd[i][0], c + dd[i][1]
            if nr < 0 or nc < 0 or nr > N - 1 or nc > M - 1:
                continue
            if box[nr][nc] == 1:
                continue
            color_near.add(box[nr][nc])

        for color in list(color_near):
            cnt += color_count[color]

        answer[r][c] = cnt % 10

for i in range(N):
    for j in range(M):
        print(answer[i][j], end="")
    print()
