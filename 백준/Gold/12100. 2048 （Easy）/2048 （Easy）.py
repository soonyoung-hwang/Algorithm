from collections import deque

N = int(input())
arr = []
for __ in range(N):
    arr.append(list(map(int,input().split())))
    
def up(arr):
    # check the each column !
    new_arr = [[0]*N for __ in range(N)]
    stack = []
    for j in range(N):
        for i in range(N):
            if(arr[i][j] == 0):
                continue
                
            if(stack and stack[-1][0] == arr[i][j] and stack[-1][1] == False):
                stack.pop()
                stack.append([2*arr[i][j],True])
            else:
                stack.append([arr[i][j],False])
        while(stack):
            v = stack.pop()
            i = len(stack)
            new_arr[i][j] = v[0]
    
    return new_arr

def down(arr):
    new_arr = [[0]*N for __ in range(N)]
    stack = []
    for j in range(N):
        for i in range(N-1,-1,-1):
            if(arr[i][j] == 0):
                continue
            if(stack and stack[-1][0] == arr[i][j] and stack[-1][1] == False):
                stack.pop()
                stack.append([2*arr[i][j],True])
            else:
                stack.append([arr[i][j],False])
        while(stack):
            v = stack.pop()
            i = N-len(stack)-1
            new_arr[i][j] = v[0]
    
    return new_arr

def left(arr):
    new_arr = [[0]*N for __ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            if(arr[i][j] == 0):
                continue
            if(stack and stack[-1][0] == arr[i][j] and stack[-1][1] == False):
                stack.pop()
                stack.append([2*arr[i][j],True])
            else:
                stack.append([arr[i][j],False])
        while(stack):
            v = stack.pop()
            j = len(stack)
            new_arr[i][j] = v[0]
    
    return new_arr

def right(arr):
    new_arr = [[0]*N for __ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N-1,-1,-1):
            if(arr[i][j] == 0):
                continue
            if(stack and stack[-1][0] == arr[i][j] and stack[-1][1] == False):
                stack.pop()
                stack.append([2*arr[i][j],True])
            else:
                stack.append([arr[i][j],False])
        while(stack):
            v = stack.pop()
            j = N-len(stack)-1
            new_arr[i][j] = v[0]
            
    return new_arr

def bfs():
    global arr
    maxi = 0
    Q = deque([])
    Q.append(arr)
    count = 5
    while(count):
        count2 = len(Q)
        while(count2):
            t = Q.popleft()
            u = up(t)
            d = down(t)
            l = left(t)
            r = right(t)
            Q.append(u)
            Q.append(d)
            Q.append(l)
            Q.append(r)
            count2 -= 1
        
        count -= 1
    
    while(Q):
        t = Q.popleft()
        for i in range(N):
            maxi = max(max(t[i]),maxi)
    
    return maxi
    
ans = bfs()
print(ans)
