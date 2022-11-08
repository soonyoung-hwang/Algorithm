T = int(input())
ts = []
for __ in range(T):
    ts.append(int(input()))

flag = False

def dfs(count, value):
    global flag
    if(flag == True):
        return
    
    if(count == 3):
        if(value == t):
            flag = True
            
        return
    
    for i in range(len(arr)):
        if(value+arr[i] > t):
            break
        else:
            dfs(count+1, value+arr[i])
    

for ii in range(T):
    t = ts[ii]

    arr = [1]
    n = 2

    while(arr[-1] < t):
        arr.append(int(n*(n+1)/2))
        n += 1
        
    flag = False
    dfs(0,0)
    if(flag):
        print(1)
    else:
        print(0)