from copy import deepcopy
import itertools
from collections import deque

MAX = 1000000
dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer = MAX

def solution(board, r, c):
    global answer
    def find(from_r, from_c, to_r, to_c):
        Q = deque()
        Q.append((from_r, from_c, 0))
        visited = [[False for _ in range(4)] for _ in range(4)]
        visited[from_r][from_c] = True
        
        while Q:
            rr, cc, count = Q.popleft()
            if (rr == to_r and cc == to_c):
                return count
            
            for i in range(4):
                # 방향키
                nr, nc = rr+dd[i][0], cc + dd[i][1]
                if (nr < 0 or nc < 0 or nr > 3 or nc > 3):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                Q.append((nr, nc, count+1))
                
            for i in range(4):
                # ctrl + 방향키
                nr, nc = rr, cc
                while (0 <= nr+dd[i][0] < 4 and 0 <= nc + dd[i][1] < 4):
                    nr, nc = nr+dd[i][0], nc+dd[i][1]
                    if board[nr][nc] != 0:
                        break
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                Q.append((nr, nc, count+1))
        return MAX
    
    def dfs(r, c, num, total):
        global answer
        r1, c1 = loc[num][0]
        r2, c2 = loc[num][1]
        
        stack.append(num) # 처리할 key 추가
        # case 1 : (r, c) -> (r1, c1) -> (r2, c2)
        new_total = total
        new_total += find(r, c, r1, c1)
        new_total += find(r1, c1, r2, c2)
        new_total += 2
        board[r1][c1] = 0
        board[r2][c2] = 0
        
        for key in all_keys:
            if key not in stack:
                dfs(r2, c2, key, new_total)
                
        if (len(stack) == L):   # 처리할 모든 key가 제거 된 상태
            answer = min(answer, new_total)
        
        board[r1][c1] = num
        board[r2][c2] = num
        
        # case 2 : (r, c) -> (r2, c2) -> (r1, c1)
        new_total = total
        new_total += find(r, c, r2, c2)
        new_total += find(r2, c2, r1, c1)
        new_total += 2
        board[r1][c1] = 0
        board[r2][c2] = 0
        
        for key in all_keys:
            if key not in stack:
                dfs(r1, c1, key, new_total)
        
        if (len(stack) == L):
            answer = min(answer, new_total)

        board[r1][c1] = num
        board[r2][c2] = num
        
        # 처리한 key 제거
        stack.pop()
        
    answer = MAX
    
    # 1. 카드별 순서 : 6! = 720
    # 2. 선/후 카드 조합 : 2^6 = 64
    # 3. 탐험하는 경우, clone 256개
    # 4. 각각의 경우, bfs (최대 6log16 * 2)
    # 너무 복잡한데? -> 출제 의도일까? -> 근데 내 계산 상 틀리진 않으니까 밀고 나가자.
    loc = dict()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in loc:
                    loc[board[i][j]] = []
                    
                loc[board[i][j]].append([i, j])
    
    all_keys = list(loc.keys())
    L = len(all_keys)
    stack = []
    for key in all_keys:
        dfs(r, c, key, 0)

            
    return answer