N, M, H = map(int,input().split())
visited = [[False]*(N) for __ in range(H+1)]
for __ in range(M):
    a, b = map(int,input().split())
    visited[a][b] = True

def check():
    global visited
    
    start = [i+1 for i in range(N)]
    for i in range(1,H+1):
        for j in range(1,N):
            if(visited[i][j] == True):
                start[j-1], start[j] = start[j], start[j-1]
    
    for i in range(N):
        if(start[i] != (i+1)):
            return False
        
    return True

def dfs(idx,cnt):
    global mini
    if(cnt > 3 or cnt >= mini):
        return
        
    if(check()):
        mini = min(mini,cnt)    
        return

    for i in range(idx,len(candi)):
        x, y = candi[i]
        if(visited[x][y-1] == True or (y+1 <= N-1 and visited[x][y+1] == True)):
            continue
        visited[x][y] = True
        dfs(i+1, cnt+1)
        visited[x][y] = False
    
    return

mini = 4
candi = []

for i in range(1,H+1):
    for j in range(1,N):
        if(visited[i][j] == True or visited[i][j-1] == True or (j+1 <= N-1 and visited[i][j+1] == True)):
            continue    
        candi.append([i,j])


        
dfs(0,0)
print(mini if mini < 4 else -1)

