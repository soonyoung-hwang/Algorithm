from collections import deque

def solution(dice):
    answer = []
    
    cases = []
    stack = []
    
    def dfs(idx, L):
        if len(stack) == L/2:
            cases.append(stack[:])
            return
        if idx >= L:
            return

        stack.append(idx)
        dfs(idx+1, L)
        stack.pop()
        dfs(idx+1, L)
    
    dfs(0, len(dice))
    
    def get_sums(target_list):
        ret = deque([0])
        target_list = deque(target_list)
        
        while target_list:
            target = dice[target_list.popleft()]
            for i in range(len(ret)):
                num = ret.popleft()
                for j in range(6):
                    ret.append(num + target[j])
        return ret
        
    
    # 2. 각 조합마다 숫자 비교하기
    max_point = 0
    
    cases = deque(cases)
    while cases:
        a = cases.popleft()
        b = cases.pop()
        
        block_1, block_2 = list(get_sums(a)), list(get_sums(b))
        block_1.sort()
        block_2.sort()
            
        point = 0
        s = 0
        for num in block_1:
            while s < len(block_1) and num > block_2[s]:
                s += 1
            point += s
            
        if point > max_point:
            max_point = point
            answer = [a[i]+1 for i in range(len(a))]
            
        point = 0
        s = 0
        for num in block_2:
            while s < len(block_1) and num > block_1[s]:
                s += 1
            point += s
        
        if point > max_point:
            max_point = point
            answer = [b[i]+1 for i in range(len(b))]
    
    return answer

