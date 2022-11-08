from collections import deque

N, M = map(int,input().split())
arr = []
for __ in range(N):
    temp = []
    s = input()
    for i in range(M):
        temp.append(int(s[i]))
    arr.append(temp)

Q = deque()
Q.append([0,0])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[-1]*M for __ in range(N)]

def bfs(x,y):
    if(x==N-1 and y==M-1):
        return 1
        
    visited[x][y] = 0
    
    count = 1
    found = False
        
    while(not found):
        if(len(Q) == 0):
            count = -1
            found = True
            break
        for i in range(len(Q)):
            q = Q.popleft()
            x, y = q[0], q[1]
            
            if([x, y] == [N-1, M-1]):
                found = True
                break

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if(0 <= nx <= N-1 and 0 <= ny <= M-1 and visited[nx][ny] != 0):
                    # not visited or visited,but 벽 깨고 온 경우... 이 안에 들어온다
                
                    # case 1 : 벽 안 깬 상태에서 길로 갔을 때
                    if(arr[nx][ny] == 0 and visited[x][y] == 0):
                        # 초행길 이거나, 방금 visited에 담긴 경우
                        if(visited[nx][ny] == -1 or count != visited[nx][ny]):
                            Q.append([nx,ny])
                        visited[nx][ny] = 0
                    
                    # case 2 : 벽 깬 상태에서 길로 갔을 때
                    elif(arr[nx][ny] == 0 and visited[x][y] >= 1):
                        # 만약 초행길이면.. Q에 넣음
                        if(visited[nx][ny] == -1):
                            Q.append([nx,ny])
                            visited[nx][ny] = count
                        
                    # case 3 : 벽 안 깬 상태에서 벽으로 갔을 때
                    elif(arr[nx][ny] == 1 and visited[x][y] == 0):
                        if(visited[nx][ny] == -1):
                            Q.append([nx,ny])
                            visited[nx][ny] = count
                        


        count += 1
    
    if(count == -1):
        return -1
    
    return count-1

a = bfs(0,0)
print(a)

