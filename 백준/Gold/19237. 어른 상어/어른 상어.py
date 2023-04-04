from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline

# Data Preprocessing

N, M ,K = map(int,input().split())
smells = [[deque() for __ in range(N)] for __ in range(N)]
sharks = defaultdict(list)              # list -> [loc(2) : tuple, direction(1) : int, coordi of smells previous(4) : deque]
sharks_to_move = defaultdict(list)      # list -> [cur_dir : 우선순위 4개]
sharks_map = [[deque() for __ in range(N)] for __ in range(N)]
is_dead = defaultdict(bool)
num_shark = M

for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j] != 0:
            sharks[temp[j]].append((i,j))           # add current location on shark

temp_2 = list(map(int,input().split()))
for i in range(M):
    sharks[i+1].append(temp_2[i])                   # add direction on shark    

    smells[sharks[i+1][0][0]][sharks[i+1][0][1]].append([K, i+1])   # update smells
    sharks_map[sharks[i+1][0][0]][sharks[i+1][0][1]].append(i+1)


# 정지, 위, 아래, 왼, 오 (0, 1, 2, 3, 4)
dd = ((0,0), (-1,0), (1,0), (0,-1), (0,1))


for i in range(M):
    for j in range(4):
        sharks_to_move[i+1].append(tuple(map(int,input().split())))


# Start
cnt = 0
while cnt < 1001:
    # 상어 움직임 + 업데이트
    for i in range(1,M+1):
        if is_dead[i]:
            continue

        cur_loc, cur_dir = sharks[i]
        r, c = cur_loc
        
        found = False
        # 1. check empty smell
        for cd in sharks_to_move[i][cur_dir-1]:
            nr, nc = r+dd[cd][0], c+dd[cd][1]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if smells[nr][nc]:
                continue
            found = True
            next_dir = cd
            next_loc = (nr, nc)
            break
        
        # 2. check smells 
        if not found:
            for cd in sharks_to_move[i][cur_dir-1]:
                nr, nc = r+dd[cd][0], c+dd[cd][1]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                
                s_list = []
                for s in smells[nr][nc]:
                    s_list.append(s[1])

                if i in s_list:
                    found = True
                    next_dir = cd
                    next_loc = (nr, nc)
                    break
        
        # 상어맵 업데이트
        sharks[i][0] = next_loc
        sharks[i][1] = next_dir

        sharks_map[r][c].pop()
        sharks_map[next_loc[0]][next_loc[1]].append(i)

    
    # 상어 충돌체크
    for i in range(N):
        for j in range(N):
            if len(sharks_map[i][j]) > 1:
                while len(sharks_map[i][j]) > 1:
                    dead = sharks_map[i][j].pop()
                    is_dead[dead] = True
                    num_shark -= 1


    # smell 맵 업데이트
    for i in range(N):
        for j in range(N):
            for k in range(len(smells[i][j])):
                smells[i][j][k][0] -= 1
            
            while smells[i][j] and smells[i][j][0][0] == 0:
                smells[i][j].popleft()
    
    # 살아남은 상어 smell 추가
    for i in range(N):
        for j in range(N):
            if sharks_map[i][j]:
                shark = sharks_map[i][j][0]
                if is_dead[shark]:
                    continue
                smells[i][j].append([K,sharks_map[i][j][0]])
        
    
    cnt += 1
    if num_shark == 1:
        break

print(cnt if cnt != 1001 else -1)