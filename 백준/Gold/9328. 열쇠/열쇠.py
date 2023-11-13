import sys
from collections import defaultdict, deque
input = sys.stdin.readline

smalls = 'abcdefghijklmnopqrstuvwxyz'
bigs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIFF = ord('A')-ord('a')
directions = ((0, 1), (0,-1), (1, 0), (-1, 0))

T = int(input())

def initialize(i, j):
    cnt = 0
    if maps[i][j] == '*':
        return 0
    if maps[i][j] == '.':
        visited[i][j] = True
        Q.append((i,j))
    elif maps[i][j] == '$':
        visited[i][j] = True
        cnt += 1
        Q.append((i,j))
    elif maps[i][j] in bigs:
        if chr(ord(maps[i][j]) - DIFF) in keys:
            visited[i][j] = True
            Q.append((i, j))
        else:
            locked[chr(ord(maps[i][j]) - DIFF)].append((i, j))

    elif maps[i][j] in smalls:
        visited[i][j] = True
        Q.append((i, j))
        if maps[i][j] not in keys:
            keys.add(maps[i][j])
            for lock in locked[maps[i][j]]:
                if not visited[lock[0]][lock[1]]:
                    visited[lock[0]][lock[1]] = True
                    Q.append((lock[0], lock[1]))

    
    return cnt

for _ in range(T):
    # preprocess
    answer = 0
    R, C = map(int,input().split())
    maps = [list(input()) for _ in range(R)]
    temp = input().rstrip()
    if temp != '0':
        keys = set(temp)
    else:
        keys = set()
    
    visited = [[False for _ in range(C)] for _ in range(R)]
    locked = defaultdict(list)
    Q = deque()

    # find entry
    for i in range(R):
        answer += initialize(i, 0)
        answer += initialize(i, C-1)
    
    for i in range(1, C-1):
        answer += initialize(0, i)
        answer += initialize(R-1, i)

    # explore
    while Q:
        r, c = Q.popleft()

        for direction in directions:
            nr, nc = r + direction[0], c + direction[1]
        
            if not(0 <= nr < R and 0 <= nc < C):
                continue
            if visited[nr][nc]:
                continue
            if maps[nr][nc] == '*':
                continue
            if maps[nr][nc] in bigs:                        # 만약 문이다.
                if chr(ord(maps[nr][nc]) - DIFF) in keys:   # 열쇠가 있다면,
                    visited[nr][nc] = True
                    Q.append((nr, nc))

                else:                                       # 열쇠가 없다면 대기 리스트에 추가
                    locked[chr(ord(maps[nr][nc]) - DIFF)].append((nr, nc))
            
            elif maps[nr][nc] in smalls:                    # 만약 키면, 새로운 Q에 추가
                visited[nr][nc] = True
                Q.append((nr, nc))
            
                if maps[nr][nc] not in keys:                # 새로 등록되는 키면,
                    keys.add(maps[nr][nc])                  # 열쇠 추가
                    for lock in locked[maps[nr][nc]]:       # 해당 추가되면서 풀리는 문들 다 Q에 넣기
                        if not visited[lock[0]][lock[1]]:
                            visited[lock[0]][lock[1]] = True
                            Q.append((lock[0], lock[1]))

            elif maps[nr][nc] == '.':
                visited[nr][nc] = True
                Q.append((nr, nc))
            
            elif maps[nr][nc] == '$':
                answer += 1
                visited[nr][nc] = True
                Q.append((nr, nc))
            
    print(answer)