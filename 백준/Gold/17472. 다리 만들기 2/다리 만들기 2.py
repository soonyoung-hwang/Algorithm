from collections import deque
import sys
import heapq

MAX = sys.maxsize

N, M = map(int,input().split())
board = [list(map(int,input().split())) for __ in range(N)]
dd = ((0,1),(0,-1),(1,0),(-1,0))


# Functions
def straight_bfs(route, i, j, C):
    Q=deque()
    visited = [[[False for __ in range(3)] for __ in range(M)] for __ in range(N)]
    visited[i][j][0] = True
    Q.append((i,j,0))
    distance = -1

    while Q:
        for i in range(len(Q)):
            r, c, state= Q.popleft()
            if board[r][c] in range(num_color+1) and board[r][c] != 0 and board[r][c] != C: # 다른 color 만났을 때,
                if distance < 2:
                    continue
                route[board[r][c]-1] = min(route[board[r][c]-1], distance)
                continue

            if state == 0:
                for i in range(4):
                    nr, nc = r + dd[i][0], c + dd[i][1]
                    if not (0<=nr<N and 0<=nc < M):
                        continue

                    if i < 2:
                        if visited[nr][nc][1]:
                            continue
                        if board[nr][nc] == C:
                            continue
                        visited[nr][nc][1] = True
                        if i < 2:
                            Q.append((nr,nc,1)) # 세로로 움직이는 bfs
                    
                    else:
                        if visited[nr][nc][2]:
                            continue
                        if board[nr][nc] == C:
                            continue
                        visited[nr][nc][2] = True
                        Q.append((nr,nc,2)) # 가로로 움직이는 bfs
            
            elif state == 1:
                for i in range(2):
                    nr, nc = r + dd[i][0], c + dd[i][1]
                    if not (0<=nr<N and 0<=nc < M):
                        continue
                    if visited[nr][nc][1]:
                        continue
                    if board[nr][nc] == C:
                        continue
                    visited[nr][nc][1] = True
                    Q.append((nr,nc,1)) # 세로로 움직이는 bfs

            elif state == 2:
                for i in range(2,4):
                    nr, nc = r + dd[i][0], c + dd[i][1]
                    if not (0<=nr<N and 0<=nc < M):
                        continue
                    if visited[nr][nc][2]:
                        continue
                    if board[nr][nc] == C:
                        continue
                    visited[nr][nc][2] = True
                    Q.append((nr,nc,2)) # 세로로 움직이는 bfs

        distance += 1

def find_minimum_routes(color1, num_color):
    # 모든 점에 대해서 직선의 bfs를 날리면 된다.
    route = [MAX for __ in range(num_color)]
    route[color1-1] = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == color1:
                straight_bfs(route, i, j, color1)
    
    return route
    



# 1. 섬의 갯수를 구하고 색을 칠한다.
visited = [[False for __ in range(M)] for __ in range(N)]

color = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        visited[i][j] = True
        board[i][j] = color
        Q = deque()
        Q.append((i,j))
        while Q:
            r, c = Q.popleft()
            for k in range(4):
                nr, nc = r + dd[k][0], c + dd[k][1]
                if not(0<=nr<N and 0<=nc<M):
                    continue
                if visited[nr][nc]:
                    continue
                if not board[nr][nc]:
                    continue
                visited[nr][nc] = True
                board[nr][nc] = color
                Q.append((nr,nc))
        
        color += 1

num_color = color-1

route = [[MAX for __ in range(M)] for __ in range(N)]

# 2. 섬 간의 최단거리를 구한다. (여기가 honey)
min_routes = []
for i in range(1, num_color+1):
    temp_r = find_minimum_routes(i, num_color)
    min_routes.append(temp_r)

# 3. 최소로 잇는 거리를 구한다.
# 0 부터 num_color-1 까지 이으면 된다.

is_connected = [False for __ in range(num_color)]
is_connected[0] = True

Q = []
for i in range(1,num_color):
    md = min_routes[0][i]
    if md == MAX:
        continue

    heapq.heappush(Q,[md, i])

min_dist = [0] + [MAX for __ in range(num_color-1)]

answer = 0
while Q:
    dis, cur = heapq.heappop(Q)
    if is_connected[cur]:
        continue
    is_connected[cur] = True
    answer += dis
    
    for i in range(num_color):
        if is_connected[i]:
            continue
        if min_routes[cur][i] == MAX:
            continue
        heapq.heappush(Q, [min_routes[cur][i], i])

print(answer if sum(is_connected) == num_color else -1)