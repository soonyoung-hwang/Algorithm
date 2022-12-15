import sys
input = sys.stdin.readline

dd = ((0,1),(0,-1),(-1,0),(1,0))
reverse = {0:1, 1:0, 2:3, 3:2}


def find_upper(mal_num):
    y, x, direction = mal_info[mal_num]
    loc = 0
    for i in range(len(map_state[y-1][x-1])):
        if mal_num == map_state[y-1][x-1][i]:
            loc = i
            break
    
    temp = []
    for i in range(loc, len(map_state[y-1][x-1])):
        temp.append(map_state[y-1][x-1][i])

    return temp


def in_range(y,x):
    return 0<y<=N and 0<x<=N

def move(mal_num):
    y, x, direction = mal_info[mal_num]
    uppers = find_upper(mal_num)
    ny, nx = y+dd[direction][0], x+dd[direction][1]
    if not in_range(ny,nx) or map_color[ny-1][nx-1] == 2:   # 벽 부딪힘 or 파랑 만남
        direction = reverse[direction]
        ny, nx = y + dd[direction][0], x + dd[direction][1]
        if in_range(ny,nx) and (map_color[ny-1][nx-1] != 2):    
            if map_color[ny-1][nx-1] == 1:
                uppers.reverse()
            for mal in uppers:
                # mal_info update
                mal_info[mal][0], mal_info[mal][1] = ny, nx
                # map_state update
                map_state[y-1][x-1].remove(mal)
                map_state[ny-1][nx-1].append(mal)
        mal_info[mal_num][2] = direction
    elif map_color[ny-1][nx-1] == 0:                        # 흰 색판
        for mal in uppers:
            # mal_info update
            mal_info[mal][0], mal_info[mal][1] = ny, nx
            # map_state update
            map_state[y-1][x-1].remove(mal)
            map_state[ny-1][nx-1].append(mal)
    elif map_color[ny-1][nx-1] == 1:                                                   # 빨간판
        uppers.reverse()
        for mal in uppers:
            # mal_info update
            mal_info[mal][0], mal_info[mal][1] = ny, nx
            # map_state update
            map_state[y-1][x-1].remove(mal)
            map_state[ny-1][nx-1].append(mal)


def turn():
    global found
    for i in range(1, K+1):
        move(i)
        if check(): # check
            found=True

def check():
    for i in range(N):
        for j in range(N):
            if len(map_state[i][j]) >= 4:
                return True



N, K = map(int,input().split())
map_color = [list(map(int,input().split())) for __ in range(N)]
map_state = [[[] for __ in range(N)] for __ in range(N)]
mal_info = dict()
for i in range(1,K+1):
    y, x, direction = map(int,input().split())
    mal_info[i] = [y, x, direction-1] # y x coordinates, direction, mal above it
    map_state[y-1][x-1].append(i)


answer = 0
found = False
while(answer < 1001):
    answer += 1
    turn()
    if found:
        break

print(answer if answer < 1001 else -1)