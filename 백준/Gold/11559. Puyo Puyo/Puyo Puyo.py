arr = [list(input().rstrip()) for _ in range(12)]
dd = ((0, 1), (0, -1), (1, 0), (-1, 0))


def try_pop(i, j):
    global is_pop
    if new_map[i][j] == ".":
        return

    visited = [[False for _ in range(12)] for _ in range(6)]
    visited[i][j] = True
    log = [(i, j)]
    stack = [(i, j)]

    cnt = 0
    while stack:
        r, c = stack.pop()
        cnt += 1
        for i in range(4):
            nr, nc = r + dd[i][0], c + dd[i][1]
            if not (0 <= nr < 6 and 0 <= nc < 12):
                continue
            if visited[nr][nc]:
                continue
            if new_map[r][c] != new_map[nr][nc]:
                continue
            visited[nr][nc] = True
            stack.append((nr, nc))
            log.append((nr, nc))

    if cnt >= 4:
        is_pop = True
        for r, c in log:
            new_map[r][c] = "."


new_map = [["." for _ in range(12)] for _ in range(6)]
for i in range(6):
    for j in range(12):
        new_map[i][j] = arr[j][i]

cnt = 0
is_pop = True
while is_pop:
    is_pop = False
    # 1. 터뜨리기
    for i in range(6):
        for j in range(12):
            try_pop(i, j)  # 4개 이상이면 터뜨리고 '.'으로 변경

    # 2. 중력작용
    for i in range(6):
        for j in range(11, -1, -1):
            if new_map[i][j] == ".":
                continue
            for k in range(11, j, -1):
                if new_map[i][k] == ".":
                    new_map[i][j], new_map[i][k] = new_map[i][k], new_map[i][j]
                    break

    if is_pop:
        cnt += 1

print(cnt)
