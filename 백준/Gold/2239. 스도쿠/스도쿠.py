possible = set([i for i in range(1, 10)])


def dfs(idx):
    global answer
    global found

    if found:
        return

    if idx == N:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            if i != 8:
                print()
        found = True
        return

    r, c = need_find[idx][0], need_find[idx][1]
    possible = [i for i in range(1, 10)]

    # 가로, 세로 체크
    for i in range(9):
        if board[i][c] in possible:
            possible.remove(board[i][c])
        if board[r][i] in possible:
            possible.remove(board[r][i])

    # box 체크
    for i in range(3):
        for j in range(3):
            if board[(r // 3) * 3 + i][(c // 3) * 3 + j] in possible:
                possible.remove(board[(r // 3) * 3 + i][(c // 3) * 3 + j])

    if not possible:
        return

    for candi in possible:
        board[r][c] = candi
        dfs(idx + 1)
        board[r][c] = 0


board = [list(map(int, input().rstrip())) for _ in range(9)]

need_find = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            need_find.append((i, j))

answer = ""
found = False

N = len(need_find)
dfs(0)