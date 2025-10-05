from collections import defaultdict
import sys
MAX_VALUE = sys.maxsize

def solution(sales, links):
    answer = 0
    
    N = len(sales)
    team = defaultdict(list)
    
    dp = [[MAX_VALUE for _ in range(N+1)] for _ in range(2)]
    
    for up, down in links:
        team[up].append(down)
    
    def find(idx, tp):
        if dp[tp][idx] != MAX_VALUE:
            return dp[tp][idx]
        
        # tp = 0 : 자기가 반드시 포함될 때
        if tp == 0:
            temp_sum = sales[idx-1]
            for down in team[idx]:
                temp_sum += min(find(down, 0), find(down, 1))
            dp[tp][idx] = min(dp[tp][idx], temp_sum)
            
        # tp = 1 : 자기가 포함 안 될때
        if tp == 1:
            if len(team[idx]) == 0:
                dp[tp][idx] = 0
            
            else:
                # 자식 중 하나 이상은 반드시 포함되어야 한다.
                for down in team[idx]:
                    temp_sum = find(down, 0)
                    for other in team[idx]:
                        if other == down:
                            continue
                        temp_sum += min(find(other, 0), find(other, 1))
                        
                    dp[tp][idx] = min(dp[tp][idx], temp_sum)
                
        return dp[tp][idx]
    
    
    answer = min(find(1, 0), find(1, 1))
    
    return answer