from collections import deque

moves = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    for _ in range(L):
        floor = list()
        for _ in range(R):
            floor.append(list(input()))
        building.append(floor)
        input()

    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    Q = deque()

    for i in range(L):
        for j in range(R):
            for c in range(C):
                if building[i][j][c] == "S":
                    visited[i][j][c] = True
                    Q.append((i, j, c, 0))

    answer = -1

    while Q:
        l, r, c, cost = Q.popleft()
        if building[l][r][c] == "E":
            answer = cost
            break

        for move in moves:
            nl, nr, nc = l + move[0], r + move[1], c + move[2]
            if not (0 <= nl < L and 0 <= nr < R and 0 <= nc < C):
                continue

            if building[nl][nr][nc] == "#":
                continue

            if visited[nl][nr][nc]:
                continue

            visited[nl][nr][nc] = True
            Q.append((nl, nr, nc, cost + 1))

    print("Trapped!" if answer == -1 else f"Escaped in {answer} minute(s).")