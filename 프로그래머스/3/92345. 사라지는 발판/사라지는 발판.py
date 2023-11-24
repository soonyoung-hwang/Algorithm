# 본 풀이는 카카오테크블로그를 참조한 풀이 입니다. 매우 어렵네요..
from copy import deepcopy
from collections import deque

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

def solution(board, aloc, bloc):
    answer = -1
    
    def OOB(r, c):
        return not (0 <= r < R and 0 <= c < C)
    
    R, C = len(board), len(board[0])
    def dfs(a, b, depth):
        win = 0
        ret = 0
        
        if depth % 2 == 0:      # A가 움직일 차례
            moved = False       # 움직일 수 있을 때,
            r, c = a
            for i in range(4):
                nr, nc = r + directions[i][0], c + directions[i][1]
                if OOB(nr, nc) or not board[nr][nc]:
                    continue
                
                moved = True
                if [r, c] == [b[0], b[1]]:
                    return 1
                
                board[r][c] = 0                
                temp_val = dfs([nr, nc], b, depth+1)
                board[r][c] = 1
                
                if temp_val % 2 == 0 and not win:           # 내가 이겼을 때,
                    win = 1
                    ret = temp_val
                elif temp_val % 2 == 0 and win:
                    ret = min(ret, temp_val)    # 가장 빠른거 선택
                elif temp_val % 2 == 1 and win: # 이번 선택은 졌지만, 한번 이겼을 때
                    continue
                elif temp_val % 2 == 1 and not win: # 이번 선택은 졌지만, 계속 졌을때
                    ret = max(ret, temp_val)                
            
            if not moved:
                return 0
            
            return ret+1
        
        else:
            moved = False       # 움직일 수 있을 때,
            r, c = b
            for i in range(4):
                nr, nc = r + directions[i][0], c + directions[i][1]
                if OOB(nr, nc) or not board[nr][nc]:
                    continue
                
                moved = True
                if [r, c] == [a[0], a[1]]:
                    return 1
                
                board[r][c] = 0
                temp_val = dfs(a, [nr, nc], depth+1)
                board[r][c] = 1
                if temp_val % 2 == 0 and not win:           # 상대방 입장 1칸 가면 내가 진거, 2칸 간거면 이긴거
                    win = 1
                    ret = temp_val
                elif temp_val % 2 == 0 and win:
                    ret = min(ret, temp_val)

                elif temp_val % 2 == 1 and not win:
                    ret = max(ret, temp_val)                
            
            if not moved:
                return 0
            
            return ret+1
        
    answer = dfs(aloc, bloc, 0)    
    
    return answer