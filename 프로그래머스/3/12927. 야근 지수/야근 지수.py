from heapq import heapify, heappush, heappop

def solution(n, works):
    answer = 0

    for i in range(len(works)):
        works[i] = -works[i]
    
    heapify(works)
    for i in range(n):
        work = heappop(works)
        if work == 0:
            break
        work += 1
        heappush(works, work)
    
    for i in range(len(works)):
        answer += works[i]**2
    
    return answer