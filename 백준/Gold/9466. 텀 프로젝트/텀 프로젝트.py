c = 0
stack = []

def loop_dfs(idx):
    global c
    stack = []
    if(visited[idx] == True):
        return
    
    visited[idx] = True
    stack.append(idx)
    
    while(True):
        if(visited[arr[stack[-1]]] == True and arr[stack[-1]] in stack):
            k = stack.index(arr[stack[-1]])
            c += k
            stack = []
            break
        elif(visited[arr[stack[-1]]] == True):
            c += len(stack)
            stack = []
            break
        else:
            visited[arr[stack[-1]]] = True
            stack.append(arr[stack[-1]])
            
T = int(input())
ns = []
arrs = []
for i in range(T):
    n = int(input())
    ns.append(n)
    arr = list(map(int,input().split()))
    arrs.append(arr)

for ii in range(T):
    n = ns[ii]
    arr = arrs[ii]
    
    for i in range(n):
        arr[i] -= 1
        
    visited = [False] * n
    # -1 means not checked yet; 0 means grouped; 1 means alone
    c = 0
    for i in range(n):
        loop_dfs(i)
    
    print(c)

