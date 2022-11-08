N, M = map(int, input().split())
a ,b, d = list(map(int,input().split()))
arr = []
for __ in range(N):
    arr.append(list(map(int,input().split())))

if(d == 1):
    d = 3
elif(d == 3):
    d = 1
    
state = [a,b,d]
count = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
repeat = 0
while(True):
    x, y, d = state
    if(arr[x][y] == 0):
        arr[x][y] = 2
        count += 1

    nd = (d+1)%4
    nx, ny = x+dx[nd], y+dy[nd]
    
    if(arr[nx][ny] == 0):
        state = [nx,ny,nd]
        repeat = 0
    
    else:
        d = nd
        state = [x,y,nd]
        repeat += 1
    
    if(repeat == 4):
        nd = (d+2)%4
        nx, ny = x+dx[nd], y+dy[nd]
        if(arr[nx][ny] != 1):
            state = [nx, ny, d]
            repeat = 0
        else:
            break

print(count)