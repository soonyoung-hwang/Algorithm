from collections import deque
import sys
input = sys.stdin.readline

input_string = list(input().rstrip())

left = deque(input_string)
right = deque()

m = int(input().rstrip())
for __ in range(m):
    command = input().rstrip()
    if command == 'L':
        if left:
            right.appendleft(left.pop())
            
    elif command == 'D':
        if right:
            left.append(right.popleft())
            
    elif command == 'B':
        if left:
            left.pop()

    else:
        t, data = command.split()
        left.append(data)
    
print(''.join(left)+''.join(right))