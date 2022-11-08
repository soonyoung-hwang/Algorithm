N, M = map(int, input().split())
arr = []
for __ in range(N):
    temp = []
    s = input()
    for i in range(M):
        temp.append(int(s[i]))
    arr.append(temp)

    
visited = [[False]*M for __ in range(N)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x,y):
    visited[x][y] = True
    current = [[x,y]]
    
    found = False
    count = 1
    
    while(not found):
        count += 1
        prev = current[:]
        current = []
        
        for i in range(len(prev)):
            add = []
            for j in range(4):
                nx = prev[i][0] + dx[j]
                ny = prev[i][1] + dy[j]
                if(0 <= nx <= N-1 and 0 <= ny <= M-1 and arr[nx][ny] == 1 and not visited[nx][ny]):
                    if(nx == N-1 and ny == M-1):
                        found = True
                        break
                    visited[nx][ny] = True
                    add.append([nx,ny])

            if(found):
                break
            else:
                current.extend(add)
        

    return count

count = bfs(0,0)
print(count)