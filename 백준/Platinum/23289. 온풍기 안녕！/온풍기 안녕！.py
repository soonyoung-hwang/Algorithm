from collections import defaultdict, deque
import sys
input = sys.stdin.readline



R, C, K = map(int,input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
machines = []

checks = set()
walls = defaultdict(bool)

for i in range(R):
    temp = list(map(int,input().split()))
    for j in range(C):
        if temp[j] == 5:
            checks.add((i, j))
        elif temp[j] != 0:
            machines.append((i, j , temp[j]))

W = int(input())
for _ in range(W):
    r, c, d = map(int,input().split())
    walls[(r,c,d)] = True

def in_range(r, c):
    return 0 <= r < R and 0 <= c < C

def check_temp():
    for r, c in checks:
        if board[r][c] < K:
            return False
    return True

# d = 1 방향이 오른쪽
# d = 2 방향이 왼쪽
# d = 3 방향이 위
# d = 4 방향이 아래
moves = ((0, 1), (0, -1), (-1, 0), (1, 0))
def wind(r, c, d, temp_board):
    move = moves[d-1]

    added = set()
    r += move[0]
    c += move[1]
    if not in_range(r, c):
        return

    temp_board[r][c] += 5
    Q = deque([(r, c, 5, 1)])
    while Q:
        r, c, p, type = Q.popleft()
        if type == 1:
            # d가 좌우면
            # 상하 dummy 주어야 함
            if (d-1) // 2 == 0:
                # 좌우
                nr1, nc1 = r - 1, c
                nr2, nc2 = r + 1, c
                if in_range(nr1, nc1):
                    if not walls[(r+1, c+1, 0)]:
                        if (nr1, nc1) not in added:
                            added.add((nr1, nc1))
                            Q.appendleft((nr1, nc1, p, 0))
                if in_range(nr2, nc2):
                    if not walls[(nr2+1, nc2+1, 0)]:
                        if (nr2, nc2) not in added:
                            added.add((nr2, nc2))
                            Q.appendleft((nr2, nc2, p, 0))

            elif (d-1) // 2 == 1:
                # 상하
                nr1, nc1 = r, c + 1
                nr2, nc2 = r, c - 1
                if in_range(nr1, nc1):
                    if not walls[(r+1, c+1, 1)]:
                        if (nr1, nc1) not in added:
                            added.add((nr1, nc1))
                            Q.appendleft((nr1, nc1, p, 0))
                if in_range(nr2, nc2):
                    if not walls[(nr2+1, nc2+1, 1)]:
                        if (nr2, nc2) not in added:
                            added.add((nr2, nc2))
                            Q.appendleft((nr2, nc2, p, 0))

        nr, nc = r + move[0], c + move[1]
        if not in_range(nr, nc):
            continue
        if (nr, nc) in added:
            continue

        if (d - 1) // 2 == 0 and not walls[(nr+1, min(nc, c)+1, 1)] \
            or (d - 1) // 2 == 1 and not walls[(max(nr, r)+1, nc+1, 0)]:

            temp_board[nr][nc] += (p-1)
            added.add((nr, nc))
            if p-1 == 0:
                continue
            Q.append((nr, nc, p-1, 1))

def operation():
    added = [[0 for _ in range(C)] for _ in range(R)]
    for r, c, d in machines:
        wind(r, c, d, added)

    for i in range(R):
        for j in range(C):
            board[i][j] += added[i][j]

def spread():
    give_board = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] <= 3:
                continue
            for i in range(4):
                move = moves[i]
                nr, nc = r + move[0], c + move[1]
                if not in_range(nr, nc):
                    continue

                if board[nr][nc] >= board[r][c]:
                    continue

                if i==0 and walls[(r+1, c+1, 1)]:
                    continue
                elif i == 1 and walls[(nr+1, nc+1, 1)]:
                    continue
                elif i == 2 and walls[(r+1, c+1, 0)]:
                    continue
                elif i == 3 and walls[(nr+1, nc+1, 0)]:
                    continue

                amount = int((board[r][c] - board[nr][nc])/4)
                give_board[nr][nc] += amount
                give_board[r][c] -= amount

    for i in range(R):
        for j in range(C):
            board[i][j] += give_board[i][j]


def decrease():
    visited = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R):
        if not visited[i][0]:
            board[i][0] = max(board[i][0]-1, 0)
            visited[i][0] = True
        if not visited[i][-1]:
            board[i][-1] = max(board[i][-1]-1, 0)
            visited[i][-1] = True

    for j in range(C):
        if not visited[0][j]:
            board[0][j] = max(board[0][j]-1, 0)
            visited[0][j] = True
        if not visited[-1][j]:
            board[-1][j] = max(board[-1][j]-1, 0)
            visited[-1][j] = True


count = 0
while count <= 100:
    operation()
    spread()
    decrease()
    
    count += 1
    if check_temp():
        break

print(count)
