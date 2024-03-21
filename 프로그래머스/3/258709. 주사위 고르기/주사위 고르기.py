from itertools import combinations
from bisect import bisect_left, bisect_right

def solution(dice):
    # answer = []
    L = len(dice)
    def new_counter_parts():
        return tuple([i for i in range(L)])
    
    def cal_value(calculated, combi, depth, max_depth, stack):
        if depth == max_depth:
            stack.append(calculated)
            return
        
        for i in range(6):
            calculated += dice[combi[depth]][i]
            cal_value(calculated, combi, depth+1, max_depth, stack)
            calculated -= dice[combi[depth]][i]
    
    def cal_diff(combi_a, combi_b):
        count = 0
        stack_a = []
        stack_b = []
        
        cal_value(0, combi_a, 0, L//2, stack_a)
        cal_value(0, combi_b, 0, L//2, stack_b)
        
        stack_b.sort()
        for num in stack_a:
            count += bisect_left(stack_b, num)
        
        return count
    
    combis = combinations([i for i in range(L)], L//2)    
    best_score = 0

    for combi in combis:
        counter_parts = set(new_counter_parts())
        counter_parts -= set(combi)
        
        score = cal_diff(list(combi), list(counter_parts))
        
        if best_score < score:
            answer = list(combi)[:]
            best_score = score
        
    for i in range(len(answer)):
        answer[i] += 1
    
    answer.sort()
    
    return answer