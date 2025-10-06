from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 무조건 하나에 걸려있어
    # before -> after
    
    # 상하좌우 본다. 길이 두 개면 옮겨탄다.
    # (or 방향이 바뀌면 -> 상하(1) 좌우(2)
    # 모든 점마다, 상하(1) 좌우(2) 박아놓는다. 3이면 교차점
    # 이 정도면, 위로갈지 아래로갈지 혹은 좌로갈지 우로갈지 모른다.
    # 또 교차면 피해가면 된다. -> inner라는 소리니까.
    
    N = 50
    box = [[0 for _ in range(N+1)] for _ in range(N+1)]
    con = [[set() for _ in range(N+1)] for _ in range(N+1)]
    
    dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
    # 0 : 위, 1 : 아래, 2 : 우, 3 : 좌
    
    # 사각형 그리기
    for x1,y1, x2,y2 in rectangle:
        for j in (y1, y2):
            for i in range(x1, x2+1):
                box[j][i] = 1
                con[j][i].add(2)
                con[j][i].add(3)
                
        for i in (x1, x2):
            for j in range(y1, y2+1):
                box[j][i] = 1
                con[j][i].add(0)
                con[j][i].add(1)        
        
        con[y1][x1].remove(1)
        con[y1][x1].remove(3)
        con[y1][x2].remove(1)
        con[y1][x2].remove(2)
        con[y2][x1].remove(0)
        con[y2][x1].remove(3)
        con[y2][x2].remove(0)
        con[y2][x2].remove(2)
        
    
    # 안에 있는거 다 0으로 죽이기
    for x1,y1, x2,y2 in rectangle:
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                box[j][i] = 0
    
    # 안에 있는거 꼭지점 아니면, 사잇길 제거
    for x1,y1, x2,y2 in rectangle:
        for i in range(x1 + 1, x2):
            con[y1][i].discard(0)
            con[y2][i].discard(1)
        
        for j in range(y1 + 1, y2):
            con[j][x1].discard(2)
            con[j][x2].discard(3)
                
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    
    Q = deque()
    Q.append((characterX, characterY, 0))
    visited[characterY][characterX] = True
    
    while Q:
        x, y, cnt = Q.popleft()

        if x == itemX and y == itemY:
            answer = cnt
            break
        
        for i in con[y][x]:
            nx, ny = x + dd[i][0], y + dd[i][1]            
            if nx > N or ny > N:
                continue
            if visited[ny][nx]:
                continue
            if box[ny][nx] == 0:
                continue
                
            visited[ny][nx] = True
            Q.append((nx, ny, cnt + 1))
        
    return answer