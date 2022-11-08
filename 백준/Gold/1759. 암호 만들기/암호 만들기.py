L, C = map(int,input().split())
arr = list(input().split())

arr.sort()
stack = []
has = [0, 0]
# has[0] -> # of 모음, has[1] -> # of 자음

is_m = [False]*26
# is_m[alphabet] 만약 alphabet이 모음이면 True, 자음이면 False

for i in range(len(is_m)):
    alphabet = chr(ord('a')+i)
    if alphabet in ('a','e','i','o','u'):
        is_m[i] = True


def dfs(index, count):
    if count == L:
        if has[0] >= 1 and has[1] >= 2:
            print(''.join(stack))
        return
    
    if index > C-1:
        return
    
    alphabet = arr[index]
    m = is_m[ord(alphabet)-ord('a')]
    
    if m:
        has[0] += 1
    else:
        has[1] += 1
    stack.append(arr[index])
    dfs(index+1, count+1)
    if m:
        has[0] -= 1
    else:
        has[1] -= 1
        
    stack.pop()
    dfs(index+1, count)

dfs(0,0)

