from collections import deque

# Brute Force
# ShiftRow - O(1)
# Rotate - O(row + column) (= 100,000)
# Operation 개수 100,000

# 자료구조 활용
# Rotate는 바깥의 줄만 영향을 받는다.
# 좌우 한 줄을 각각 deque로 하고,
# 가운데 한 줄을 deque로 받는다.

def solution(rc, operations):
    answer = []
    R, C = len(rc), len(rc[0])    
    sides = deque([deque([]), deque([])])
    middles = deque([deque([0 for _ in range(C-2)]) for _ in range(R)])
    
    for i in range(R):
        sides[0].append(rc[i][0])
        sides[1].append(rc[i][-1])
    
        
    for i in range(R):
        for j in range(1, C-1):
            middles[i][j-1] = rc[i][j]
    
    def rotate():
        if middles[0]:
            s1 = sides[0].popleft()
            s2 = middles[0].pop()
            s3 = sides[1].pop()
            s4 = middles[-1].popleft()
            sides[0].append(s4)
            middles[0].appendleft(s1)
            sides[1].appendleft(s2)
            middles[-1].append(s3)
            return
        
        s1 = sides[0].popleft()
        s2 = sides[1].pop()
        sides[0].append(s2)
        sides[1].appendleft(s1)
        
        return
    
    
    def shiftrow():
        sides[0].appendleft(sides[0].pop())
        sides[1].appendleft(sides[1].pop())
        if middles[0]:
            middles.appendleft(middles.pop())
        
    for operation in operations:
        if operation == "Rotate":
            rotate()
        elif operation == "ShiftRow":
            shiftrow()
            
    for i in range(R):
        answer.append([sides[0][i], *middles[i] ,sides[1][i]])
    
    return answer