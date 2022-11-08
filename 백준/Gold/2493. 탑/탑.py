import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))

stack = []
ans = []
for i in range(N):
    if(len(stack)==0):
        stack.append([i,arr[i]])
        ans.append(0)
    else:
        while(len(stack) >= 1 and stack[-1][1] < arr[i]):
            stack.pop()
    
        if(len(stack)==0):
            ans.append(0)
        else:
            ans.append(stack[-1][0]+1)
        
        stack.append([i,arr[i]])
        

print(*ans)