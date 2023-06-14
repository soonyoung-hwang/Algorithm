from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

def rotate(board, r, c, S):
    for i in range(1, S+1):
        rotate_line(board, r, c, i)

def rotate_line(board, r, c, S):
    # rotate the board, return nothing.
    # center : (n, c)
    # radius : S
    # method : put all the regarding values into a deque, and rotate it, and assign them again.

    for_rotate = deque()
    cur = [r-S, c-S]
    for d in range(4):
        for i in range(2*S):
            for_rotate.append(board[cur[0]][cur[1]])
            cur[0] += direction[d][0]
            cur[1] += direction[d][1]
    
    for_rotate.appendleft(for_rotate.pop())
    cur = [r-S, c-S]
    
    for d in range(4):
        for i in range(2*S):
            board[cur[0]][cur[1]] = for_rotate.popleft()
            cur[0] += direction[d][0]
            cur[1] += direction[d][1]

def calculate(board) -> int:
    # find the min sum and return it
    mini = 5_001
    for i in range(N):
        mini = min(mini, sum(board[i]))
    return mini

def backtracking(board, cnt):
    global answer

    if cnt > K-1:
        answer = min(answer, calculate(board))
        return

    for i in range(K):
        if visited[i]:
            continue
        
        visited[i] = True
        new_board = deepcopy(board)
        # rotate new_board
        r, c, s = commands[i]
        rotate(new_board, r-1, c-1, s)
        backtracking(new_board, cnt+1)        
        visited[i] = False
    


N, M, K = map(int,input().split())
origin_board = [list(map(int,input().split())) for _ in range(N)]
commands = [list(map(int,input().split())) for _ in range(K)]
visited = [False for i in range(K)]

answer = 5_001
backtracking(origin_board, 0)
print(answer)