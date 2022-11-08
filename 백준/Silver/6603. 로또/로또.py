
def dfs(d, idx, arr):
    if(d == 6):
        print(*stack)
#         stack.pop()
        return
    

    for i in range(idx,len(arr)-(6-d)+1):
        stack.append(arr[i])
        dfs(d+1, i+1, arr)
        stack.pop()
        

arrs = []
while(True):
    s = input()
    if(s=='0'):
        break
    arrs.append(list(map(int,s.split())))

for ii in range(len(arrs)):
    n = arrs[ii][0]
    arr = arrs[ii][1:]
    stack = []
    dfs(0, 0, arr)
    print("")
    
    