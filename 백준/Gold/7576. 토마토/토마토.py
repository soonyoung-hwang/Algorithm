def bfs(start):
    current = start
    count = 0
    
    while(current):
        prev = current[:]
        current = []
        
        for i in range(len(prev)):
            add = []
            for j in range(4):
                nx = prev[i][0] + dx[j]
                ny = prev[i][1] + dy[j]
                if(0 <= nx <= N-1 and 0 <= ny <= M-1 and arr[nx][ny] == 0):
                    arr[nx][ny] = 1
                    add.append([nx,ny])

            current.extend(add)
        
        count += 1

    return count-1

M, N = map(int,input().split())
arr = []
for __ in range(N):
    arr.append(list(map(int,input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

start = []
for i in range(N):
    for j in range(M):
        if(arr[i][j] == 1):
            start.append([i,j])

count = bfs(start)

for i in range(N):
    for j in range(M):
        if(arr[i][j] == 0):
            count = -1
            break

print(count)