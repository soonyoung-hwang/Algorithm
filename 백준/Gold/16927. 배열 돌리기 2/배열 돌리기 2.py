from collections import deque

def rotate(r, c, n, m, count):
    Q = deque()
    for i in range(n-1):
        Q.append(board[r+i][c])
    for i in range(m-1):
        Q.append(board[r+n-1][c+i])
    for i in range(n-1):
        Q.append(board[r+n-(i+1)][c+m-1])
    for i in range(m-1):
        Q.append(board[r][m+c-(i+1)])
    
    for _ in range(count):
        Q.appendleft(Q.pop())
    
    for i in range(n-1):
        answer_board[r+i][c] = Q.popleft()
    for i in range(m-1):
        answer_board[r+n-1][c+i] = Q.popleft()
    for i in range(n-1):
        answer_board[r+n-(i+1)][c+m-1] = Q.popleft()
    for i in range(m-1):
        answer_board[r][m+c-(i+1)] = Q.popleft()

N, M, R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer_board = [[0 for _ in range(M)] for _ in range(N)]

for i in range(0, min(N, M)//2):
    n, m = N - 2 * i, M - 2 * i
    cycle = 2 * m + 2 * n - 4
    count = R % cycle
    rotate(i, i, n, m, count)

for i in range(N):
    print(*answer_board[i])