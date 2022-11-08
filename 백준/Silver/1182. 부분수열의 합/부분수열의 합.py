N, S = map(int,input().split())
arr = list(map(int,input().split()))

count = 0

def dfs_back(value,num,idx):
    global count
    #print(value,num,idx)
    
    if(value == S and num >= 1):
        count += 1
    
    if(num >= N):
        return
    
    for i in range(idx, N):
        dfs_back(value+arr[i],num+1,i+1)
    
    return

dfs_back(0,0,0)
print(count)