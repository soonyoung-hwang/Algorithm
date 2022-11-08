from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int,input().split())
tmt = [[list(map(int,input().split())) for __ in range(N)] for __ in range(H)]
dd = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
# tomato at x,y,z : tmt[z][x][y]

# size : 1,000,000
# maximum days : 100+100+100 : 300 days
# total : 300,000,000 : 3억
# 최적화 필요

def in_range(x,y,z):
    return 0 <= x < N and 0 <= y < M and 0 <= z < H
                    
def is_all_matured():
    for i in range(N):
        for j in range(M):
            for k in range(H):
                if tmt[k][i][j] == 0:
                    return False     
    return True


checked = [[[False for __ in range(M)] for __ in range(N)] for __ in range(H)]
Q = deque()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if tmt[k][i][j] == 1:
                Q.append([i, j, k, 0])
                checked[k][i][j] = True

days = 0
while Q:
    x, y, z, d = Q.pop()
    days = max(days, d)
    
    for dx, dy, dz in dd:
        nx, ny, nz = x+dx, y+dy, z+dz
        if not in_range(nx,ny,nz):
            continue
        if checked[nz][nx][ny]:
            continue
        if tmt[nz][nx][ny] == -1:
            continue
        if tmt[nz][nx][ny] == 1:
            continue
        tmt[nz][nx][ny] = 1
        checked[nz][nx][ny] = True
        Q.appendleft([nx, ny, nz, d+1])

if is_all_matured():
    answer = days
else:
    answer = -1

print(answer)