def solution(n, s):
    answer = []
    
    temp_s = s
    for i in range(n, 1, -1):
        if temp_s % i > 0:
            answer.append(temp_s//i + 1)
            temp_s -= (temp_s//i + 1)
        else:
            answer.append(temp_s//i)
            temp_s -= (temp_s//i)
    
    answer.append(s - sum(answer))
    
    for i in range(n):
        if answer[i] <= 0:
            answer = [-1]
            break
            
    answer.sort()
    
    return answer