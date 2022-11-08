n = int(input())
mapp = []
for _ in range(n):
    temp = []
    s = input()
    for i in range(n):
        temp.append(int(s[i]))
    mapp.append(temp)

def dfs(x,y):
    global count
    count += 1
    
    mapp[x][y] = 0
    
    if(x-1 >= 0 and mapp[x-1][y] == 1):
        dfs(x-1,y)
    if(x+1 <= n-1 and mapp[x+1][y] == 1):
        dfs(x+1,y)
    if(y-1 >= 0 and mapp[x][y-1] == 1):
        dfs(x,y-1)
    if(y+1 <= n-1 and mapp[x][y+1] == 1):
        dfs(x,y+1)

answer = []
for i in range(n):
    for j in range(n):
        if(mapp[i][j] == 1):
            count = 0
            dfs(i,j)
            answer.append(count)
            
answer.sort()
print(len(answer))
for a in answer:
    print(a)
