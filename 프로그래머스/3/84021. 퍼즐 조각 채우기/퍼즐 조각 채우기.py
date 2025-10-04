import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

dd = ((0, 1), (0, -1), (1, 0), (-1, 0))

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    # table을 네 방향 돌려서 각각 방향마다 game board에 대입되는거 있으면 서로 업데이트 해주기
    
    def dfs(r, c, color, route):
        for i in range(4):
            nr, nc = r + dd[i][0], c + dd[i][1]
            if nr < 0 or nc < 0 or nr > N-1 or nc > N-1:
                continue
            if color == 0:
                if table[nr][nc] == 0:
                    continue
            if color == 1:
                if game_board[nr][nc] == 1:
                    continue
            if visited[nr][nc]:
                continue
            route.append(i)
            shape.append(tuple(route))
            visited[nr][nc] = True
            dfs(nr, nc, color, route)
            route.pop()
        
    # 게임보드
    visited = [[False for _ in range(N)] for _ in range(N)]
    shape_board = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 1:
                continue
            if visited[i][j]:
                continue
            shape = []
            visited[i][j] = True
            dfs(i, j, 1, [])
            shape = tuple(shape)
            shape_board[shape].append((i, j))
    
    
    # rotated table
    for i in range(4):
        for i in range((N+1)//2):
            for j in range(N//2):
                table[j][N-1-i], table[N-1-i][N-1-j], table[N-1-j][i], table[i][j]  \
                     = table[i][j], table[j][N-1-i], table[N-1-i][N-1-j], table[N-1-j][i]
        visited = [[False for _ in range(N)] for _ in range(N)]
        shape_table = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if table[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                shape = []
                visited[i][j] = True
                dfs(i, j, 0, [])
                shape = tuple(shape)
                shape_table[shape].append((i, j))

        for kk in shape_table.keys():
            for r, c in shape_table[kk]:
                if len(shape_board[kk]):
                    # 보드에 블록 채우기
                    shape_board[kk].pop()
                    answer += (len(kk) + 1)

                    # 블록 테이블에서 빼기
                    table[r][c] = 0
                    for each_loc in kk:
                        nr, nc = r, c
                        for num in each_loc:
                            nr += dd[num][0]
                            nc += dd[num][1]
                        table[nr][nc] = 0
    
    return answer