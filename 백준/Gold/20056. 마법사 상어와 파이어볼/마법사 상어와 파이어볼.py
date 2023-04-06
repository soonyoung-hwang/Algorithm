import sys
from copy import deepcopy

input = sys.stdin.readline


N, M ,K = map(int,input().split())
board = [[[] for __ in range(N)] for __ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    board[r-1][c-1].append((m,s,d))


dd = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1,0), (1,-1), (0,-1), (-1,-1))



def cycle():
    # 1. move balls
    new_board = [[[] for __ in range(N)] for __ in range(N)]
    
    for r in range(N):
        for c in range(N):
            while board[r][c]:
                m, s, d = board[r][c].pop()
                
                nr, nc = (r + dd[d][0]*s)%N, (c + dd[d][1]*s)%N
                new_board[nr][nc].append((m, s, d))

    for r in range(N):
        for c in range(N):
            if len(new_board[r][c]) < 2:
                continue

            # 합쳐지는게 모두 짝수 or 홀수는 어떻게 하지??
            all_even = True
            all_odd = True

            m_total = 0
            s_total = 0
            L = len(new_board[r][c])
            while new_board[r][c]:
                m, s, d = new_board[r][c].pop()
                m_total += m
                s_total += s
                
                if d%2 == 1:
                    all_even = False
                else:
                    all_odd = False
            
            added = 0 if all_even or all_odd else 1
            
            if m_total//5 == 0:
                continue

            for i in range(4):
                new_board[r][c].append((m_total//5, s_total//L, i*2+added))


    return new_board


cnt = 0
while cnt < K:
    board = cycle()
    cnt += 1


answer = 0
for i in range(N):
    for j in range(N):
        for k in range(len(board[i][j])):
            answer += board[i][j][k][0]

print(answer)