N = int(input())
arr = []
for __ in range(N):
    arr.append(list(map(int,input().split())))
    
maxi = 0
def dfs(idx, value):
    global maxi
    if(idx > N-1):
        maxi = max(maxi, value)
        return
        
    t, p = arr[idx]
    if(idx+t <= N):
        dfs(idx+t, value+p)
    dfs(idx+1, value)
    
dfs(0,0)
print(maxi)