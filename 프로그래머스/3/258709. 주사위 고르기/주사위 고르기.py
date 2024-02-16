from itertools import combinations
from bisect import bisect_left, bisect_right

def solution(dice):
    answer = []
    for i in range(len(dice)):
        dice[i].sort()
    
    print(dice)
    
    
#     def new_counter_parts():
#         return tuple([i for i in range(len(dice))])
    
#     def calculate_score(combi_a, combi_b):
        
    
#     combis = combinations([i for i in range(len(dice))], len(dice)//2)
#     done = set()
    
#     for combi in combis:
#         counter_parts = set(new_counter_parts())
#         counter_parts -= set(combi)
        
#         if frozenset(combi) in done:
#             continue
        
#         done.add(frozenset(combi))
#         done.add(frozenset(counter_parts))
        
#         diff = calculate_score(combi, tuple(counter_parts))

    
    return answer