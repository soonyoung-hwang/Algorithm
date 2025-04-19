def solution(players, m, k):
    answer = 0
    
    possible = [0 for _ in range(24)]
    
    for i in range(24):
        if i > 0:
            possible[i] += possible[i-1]
        
        need = players[i] // m
        if possible[i] < need:
            plus = need-possible[i]
            answer += plus
            
            possible[i] += plus
            if i+k < 24:
                possible[i+k] -= plus
    
    return answer