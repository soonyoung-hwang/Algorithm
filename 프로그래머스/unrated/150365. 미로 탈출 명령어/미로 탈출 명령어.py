from collections import deque
import sys
sys.setrecursionlimit(10**6)

dd = ((1,0),(0,-1),(0,1),(-1,0))

answer = ''
def solution(n, m, x, y, r, c, k):
    global answer
    r -= 1
    c -= 1
    
    visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    stack = []
    def dfs(x, y, cnt):
        global answer
        if answer:
            return
        
        if cnt == k:
            if x == r and y == c:
                answer = ''.join(stack)
                return
            return
        
        for i in range(4):
            nx, ny = x + dd[i][0], y + dd[i][1]
            if not (0 <= nx < n and 0 <= ny < m): continue
            if visited[nx][ny][cnt]: continue
            visited[nx][ny][cnt] = True
            if i == 0:
                stack.append('d')
            elif i == 1:
                stack.append('l')
            elif i == 2:
                stack.append('r')
            elif i == 3:
                stack.append('u')
                
            dfs(nx, ny, cnt+1)
            stack.pop()
    
    dfs(x-1,y-1,0)    
    if not answer:
        answer = 'impossible'
            
            
                    
            
    
    return answer