# 5427 불 : 상근이는 화재를 피해 건물을 탈출해야 한다.

# 건물 탈출 조건 : 건물의 모서리
# 불은 매초 상하좌우로 퍼짐, 벽에는 안 퍼짐
# 불이 먼저 움직인다고 가정 (불은 상근이를 덮을 수도 있다) -> 다음 턴에 피하면 된다.
# 그래야 상근이가 움직일 수 있는 지점들이 명확해진다.

import sys
input = sys.stdin.readline

from collections import deque

def clear(c, r, pc, pr):
    return (pc == 0 or pc == c-1 or pr == 0 or pr == r-1)

def in_range(c,r, pc,pr):
    return ((0 <= pc < c) and (0<= pr < r))

dd = ((0,1), (1,0), (0,-1), (-1,0))


T = int(input())
for __ in range(T):
    c, r = map(int,input().split())
    arr = [list(input().rstrip()) for __ in range(r)]
    sgs = deque([])
    fires = deque([])
    found = False
    answer = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '*':
                fires.append((i,j))
            elif arr[i][j] == '@':
                sgs.append((i,j))
    
    while not found and (fires or sgs): # 정답을 못찾고 더 탐험할 불 혹은 상근이가 있을 때만 계속 진행
        answer += 1
        for i in range(len(fires)):     # 불 움직임
            pr, pc = fires.popleft()
            for d in dd:
                nr, nc = pr + d[0], pc + d[1]
                if not in_range(c,r,nc,nr):
                    continue
                elif arr[nr][nc] == '*':
                    continue
                elif arr[nr][nc] == '#':
                    continue
                arr[nr][nc] = '*'
                fires.append((nr,nc))
        
        for i in range(len(sgs)):       # 상근 움직임
            pr, pc = sgs.popleft()
            if clear(c,r,pc,pr):        # 만약 다음 상근이가 클리어지점이면 끝내기.
                found = True
                break
            for d in dd:
                nr, nc = pr + d[0], pc + d[1]
                if not in_range(c,r,nc,nr):
                    continue
                elif arr[nr][nc] == '*':
                    continue
                elif arr[nr][nc] == '#':
                    continue
                elif arr[nr][nc] == '@':
                    continue
                arr[nr][nc] = '@'
                sgs.append((nr,nc))
    
    print(answer if found else "IMPOSSIBLE")