from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

M, S = map(int,input().split())
fish_map = [[deque([]) for _ in range(4)] for _ in range(4)]
smell_map = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(int,input().split())
    fish_map[r-1][c-1].append(d-1)

shark_a, shark_b = map(int,input().split())
shark = [shark_a-1, shark_b-1]

moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
shark_moves = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            shark_moves.append((moves[i], moves[j], moves[k]))

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
fish_moves = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

def in_range(r, c):
    return 0 <= r < 4 and 0 <= c < 4
def fish_move():
    after_fish = [[deque([]) for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            Q = fish_map[r][c]
            for i in range(len(Q)):
                d = Q.popleft()
                for j in range(d, d-8, -1):
                    move = fish_moves[j%8]
                    nr, nc = r + move[0], c + move[1]
                    if not in_range(nr, nc):
                        continue
                    if (shark[0], shark[1]) == (nr, nc):
                        continue
                    if smell_map[nr][nc]:
                        continue
                    after_fish[nr][nc].append(j % 8)
                    break
                else:
                    Q.append(d)
    for r in range(4):
        for c in range(4):
            while after_fish[r][c]:
                fish_map[r][c].append(after_fish[r][c].popleft())


def shark_move():
    global shark
    temp_r, temp_c = -1, -1
    value = -1
    best_i = -1
    for i in range(64):
        visited = [[False for _ in range(4)] for _ in range(4)]
        moves = shark_moves[i]
        temp_r, temp_c = shark
        temp_value = 0
        move_count = 0
        for move in moves:
            nr, nc = temp_r + move[0], temp_c + move[1]
            if not in_range(nr, nc):
                break
            if not visited[nr][nc]:
                temp_value += len(fish_map[nr][nc])
            visited[nr][nc] = True
            move_count += 1
            temp_r, temp_c = nr, nc
        if move_count == 3:
            if value < temp_value:
                value = temp_value
                best_i = i


    r, c = shark
    moves = shark_moves[best_i]
    for move in moves:
        nr, nc = r + move[0], c + move[1]
        if fish_map[nr][nc]:
            fish_map[nr][nc] = deque([])
            smell_map[nr][nc] = 3
        r, c = nr, nc

    shark = [nr, nc]

def smell_gone():
    for i in range(4):
        for j in range(4):
            if smell_map[i][j] > 0:
                smell_map[i][j] -= 1

def duplicate():
    for r in range(4):
        for c in range(4):
            while duplicated[r][c]:
                fish_map[r][c].append(duplicated[r][c].popleft())

for _ in range(S):
    duplicated = deepcopy(fish_map)
    fish_move()
    shark_move()
    smell_gone()
    duplicate()

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(fish_map[i][j])

print(answer)

