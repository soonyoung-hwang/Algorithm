# # # 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
# # # 연구소의 크기 N(4 ≤ N ≤ 50), 바이러스의 개수 M(1 ≤ M ≤ 10)
# # # 16 ≤ N by N ≤ 2500
# # # Maximum step : 2500
import itertools
from collections import deque
import copy

Dir = ((0,1),(0,-1),(1,0),(-1,0))

def in_range(x,y):
    return 0<=x<N and 0<=y<N
    
def bfs(activated_virus, total_virus):
    Q = deque()
    lab = copy.deepcopy(labs)
    visited = [[False for __ in range(N)] for __ in range(N)]
    walls = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 1:
                walls += 1
                
    goal = N*N - walls
    num_virus = total_virus
    
    for virus in activated_virus:
        Q.append(virus+[0])
        visited[virus[0]][virus[1]] = True
        
    s = -1
    while Q and num_virus != goal:
        if num_virus == goal:
            break
        
        x, y, s = Q.popleft()
        for d in Dir:
            nx, ny = x+d[0], y+d[1]
            if not in_range(nx,ny):
                continue
            if lab[nx][ny] == 1:
                continue
            if visited[nx][ny]:
                continue
                
            if lab[nx][ny] != 2:
                num_virus += 1

            visited[nx][ny] = True
            lab[nx][ny] = 2
            Q.append([nx,ny,s+1])

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                return INF
        
    return s+1

N, M = map(int,input().split())
labs = [list(map(int,input().split())) for __ in range(N)]

viruses = []
for i in range(N):
    for j in range(N):
        if labs[i][j] == 2:
            viruses.append([i,j])

activateds = list(itertools.combinations(viruses,M))


INF = 2501
answer = INF
num_v = len(viruses)

for activate in activateds:
    answer = min(answer,bfs(activate, num_v))

print(answer if answer != INF else -1)