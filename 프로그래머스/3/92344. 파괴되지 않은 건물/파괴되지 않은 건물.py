def solution(board, skill):    
    N, M = len(board), len(board[0])
    damage = [[0 for _ in range(M)] for _ in range(N)]
    for Q in skill:
        tp, r1, c1, r2, c2, degree = Q
        damage[r1][c1] += (-1)**tp * degree
        if (c2 < M-1):
            damage[r1][c2+1] += -1 * ((-1)**tp) * degree
        if (r2 < N-1):
            damage[r2+1][c1] += -1 * ((-1)**tp) * degree
        if (c2 < M-1 and r2 < N-1):
            damage[r2+1][c2+1] += ((-1)**tp) * degree
        
    for i in range(N):
        for j in range(1, M):
            damage[i][j] += damage[i][j-1]
    
    for i in range(M):
        for j in range(1, N):
            damage[j][i] += damage[j-1][i]
    
    for i in range(N):
        for j in range(M):
            board[i][j] += damage[i][j]
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt += 1
    
    return cnt