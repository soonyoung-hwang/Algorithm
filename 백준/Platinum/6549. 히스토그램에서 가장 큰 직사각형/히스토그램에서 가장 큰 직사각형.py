while True:
    L = list(map(int,input().split()))
    N = L[0]
    if N == 0:
        break
    arr = L[1:]

    stack = []
    temp = []

    for i in range(N):
        n = arr[i]
        t = i
        if not stack:
            stack.append([n,i])
            continue
            
        while stack and n < stack[-1][0]:
            cv, ci = stack.pop()
            t = ci
            temp.append(cv*(i-ci))
        
        stack.append([n,t])
    
    while stack:
        cv, ci = stack.pop()
        temp.append(cv*(N-ci))
    
    print(max(temp))

