# 선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 작은 선거구의 인구 차이의 최솟 값
# 5 <= N <= 20 , 완탐이 될까, 그리디로 접근해야 하나?, back tracking 해야 하나?
# N by N : 400 - x,y 좌표의 조합 400 * 400 160000 * 400      
import sys
input = sys.stdin.readline

def calculate_diff(x, y, d1, d2, N):
    global arr
    
    mapp = [[-1 for __ in range(N+1)] for __ in range(N+1)]
    end_lines = ((x+d1-1, y), (x+d2,y+1), (x+d1, y-d1+d2-1), (x+d2+1, y-d1+d2)) # includes
    
    boundary = []
    for i in range(d1+1):
        nx, ny = x+i, y-i
        boundary.append((nx,ny))
        nx, ny = x+d2+i, y+d2-i
        boundary.append((nx,ny))
    
    for i in range(d2+1):
        nx, ny = x+i, y+i
        boundary.append((nx,ny))
        nx, ny = x+d1+i, y-d1+i
        boundary.append((nx,ny))
    
    boundary = set(boundary)
    for x,y in boundary:
        mapp[x][y] = 5
    
    for x in range(1,end_lines[0][0]+1):
        for y in range(1,end_lines[0][1]+1):
            if mapp[x][y] == 5:
                break
            else:
                mapp[x][y] = 1
    
    for x in range(1,end_lines[1][0]+1):
        for y in range(N,end_lines[1][1]-1,-1):
            if mapp[x][y] == 5:
                break
            else:
                mapp[x][y] = 2

    for x in range(N,end_lines[2][0]-1,-1):
        for y in range(1,end_lines[2][1]+1):
            if mapp[x][y] == 5:
                break
            else:
                mapp[x][y] = 3
                
    for x in range(N,end_lines[3][0]-1,-1):
        for y in range(N,end_lines[3][1]-1,-1):
            if mapp[x][y] == 5:
                break
            else:
                mapp[x][y] = 4

#     for i in range(len(mapp)):
#         print(*mapp[i])
    
    total = (N*N)
    max_val = 0
    min_val = 40000
    for n in range(5):
        t = 0
        for i in range(N):
            for j in range(N):
                if mapp[i+1][j+1] == -1:
                    mapp[i+1][j+1] = 5
                if mapp[i+1][j+1] == n+1:
                    t += arr[i][j]
        
        max_val = max(max_val,t)
        min_val = min(min_val,t)
                    
    return max_val - min_val

N = int(input())
arr = [list(map(int,input().split())) for __ in range(N)]

answer = 40000

def in_range(x,y):
    return 0 < x < N+1 and 0 < y < N+1

# size : 400 * 400 
for x in range(1,N+1):
    for y in range(1,N+1):
        if x == 1 and y == 1: continue
        elif x == N and y == N : continue
        elif x == N and y == 1 : continue
        elif x == 1 and y == N : continue
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if not in_range(x+d1,y-d1) or not in_range(x+d2,y+d2) or \
                not in_range(x+d1+d2,y-d1+d2):
                    continue
                temp = calculate_diff(x,y,d1,d2,N)
                if answer > temp:
                    answer = temp
                
print(answer)
