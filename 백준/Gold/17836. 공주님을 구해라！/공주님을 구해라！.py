from collections import deque

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]

visited[0][0][0] = True
Q = deque([(0, 0, 0, 0)])  # r, c, time, weapon


answer = -1
while Q:
    r, c, time, weapon = Q.popleft()

    if r == N - 1 and c == M - 1:
        if time <= T:
            answer = time
        break

    for move in moves:
        nr, nc = r + move[0], c + move[1]
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nr][nc][weapon]:
            continue

        if not weapon:
            if board[nr][nc] == 1:
                continue
            elif board[nr][nc] == 0:
                visited[nr][nc][0] = True
                Q.append((nr, nc, time + 1, 0))
            else:
                visited[nr][nc][0] = True
                visited[nr][nc][1] = True
                Q.append((nr, nc, time + 1, 1))

        else:
            visited[nr][nc][1] = True
            Q.append((nr, nc, time + 1, 1))

print(answer if answer != -1 else "Fail")