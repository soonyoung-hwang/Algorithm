N = int(input())
arr = []
for __ in range(N):
    arr.append(list(map(int,input().split())))
    
def next_g(L):
    # next generation of current indices.
    temp = []
    dx = L[-1][0]
    dy = L[-1][1]

    for i in range(len(L)-2,-1,-1):
        x = L[i][0]
        y = L[i][1]
        nx = -y+dy+dx
        ny = x-dx+dy
        temp.append([nx,ny])
    
    L.extend(temp)
    

visited = [[False]*101 for __ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    dragon = arr[i]
    x, y, d, g = dragon
    L = [[x,y]]
    L.append([x+dx[d],y+dy[d]])
    for j in range(g):
        next_g(L)

    for j in range(len(L)):
        visited[L[j][0]][L[j][1]] = True

count = 0
for i in range(100):
    for j in range(100):
        if(visited[i][j] == True and visited[i+1][j] == True
           and visited[i][j+1] == True and visited[i+1][j+1] == True):
            count += 1

print(count)
