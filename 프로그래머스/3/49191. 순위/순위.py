from collections import defaultdict

def solution(n, results):
    answer = 0
    
    before, after = defaultdict(set), defaultdict(set)
    for winner, loser in results:
        after[winner].add(loser)
        for num in list(before[winner]):
            after[num].add(loser)
            before[loser].add(num)
                    
        before[loser].add(winner)
        for num in list(after[loser]):
            before[num].add(winner)
            after[winner].add(num)
            
        for win_part in list(before[winner]):
            for lose_part in list(after[loser]):
                before[lose_part].add(win_part)
                after[win_part].add(lose_part)
                
    for num in range(1, n+1):
        if len(before[num]) + len(after[num]) == n-1:
            answer += 1
    
    return answer