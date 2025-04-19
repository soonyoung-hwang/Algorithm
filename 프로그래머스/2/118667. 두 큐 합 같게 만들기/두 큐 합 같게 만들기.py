from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    N = len(queue1)
    
    q1, q2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    
    for i in range(4*N):
        if sum_q1 == sum_q2:
            answer = i
            break
        elif sum_q1 > sum_q2:
            num = q1.popleft()
            sum_q1 -= num
            sum_q2 += num
            q2.append(num)
        else:
            num = q2.popleft()
            sum_q1 += num
            sum_q2 -= num
            q1.append(num)
        
    return answer