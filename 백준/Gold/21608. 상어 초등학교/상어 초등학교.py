import sys

input = sys.stdin.readline

N = int(input())
current = [[-1 for _ in range(N)] for _ in range(N)]
total_likes = [[] for _ in range(N**2+1)]
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer = 0

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def find_empty(r, c):
    ret = 0
    for move in moves:
        nr, nc = r + move[0], c + move[1]
        if not in_range(nr, nc):
            continue
        if current[nr][nc] != -1:
            continue
        ret += 1

    return ret

def find_likes(r, c, likes):
    ret = set()
    for move in moves:
        nr, nc = r + move[0], c + move[1]
        if not in_range(nr, nc):
            continue
        if current[nr][nc] == -1:
            continue
        ret.add(current[nr][nc])

    return len(ret.intersection(likes))


for _ in range(N**2):
    temp = list(map(int,input().split()))
    student = temp[0]
    likes = temp[1:]
    total_likes[student].extend(likes)

    temp_like = -1
    temp_empty = -1
    r = 0
    c = 0

    for i in range(N):
        for j in range(N):
            if current[i][j] != - 1:
                continue

            like = find_likes(i, j, likes)
            empty = find_empty(i, j)

            if like > temp_like:
                temp_like = like
                temp_empty = empty
                r, c = i, j
                continue

            if like == temp_like and empty > temp_empty:
                r, c = i, j
                temp_empty = empty
                continue

    current[r][c] = student

for i in range(N):
    for j in range(N):
        like = find_likes(i, j, total_likes[current[i][j]])
        answer += int(10**(like-1))

print(answer)