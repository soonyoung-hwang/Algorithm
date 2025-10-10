import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = 0
    
    # n개의 괄호쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 개수
    # n개의 쌍이면 ( 가 n개 (n <= 14)
    temp = [0]
    used = [0]
    stack = []
    
    def dfs(idx):
        if idx == n*2:
            temp[0] += 1
            return
        
        if not stack and used[0] == n:
            # 잘못 된 접근으로 생성된 것 -> 끝
            return
        
        if used[0] < n:
            used[0] += 1
            stack.append('a')
            # 새롭게 열기
            dfs(idx+1)
            used[0] -= 1
            stack.pop()
            
        if stack:
            stack.pop()
            dfs(idx+1)
            stack.append('a')
            
    dfs(0)
    answer = temp[0]
    
    return answer