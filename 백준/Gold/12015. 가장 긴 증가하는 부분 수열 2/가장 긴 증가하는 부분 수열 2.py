from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

stack = []

for num in arr:
    if not stack:
        stack.append(num)
        continue
    
    if num > stack[-1]:
        stack.append(num)
        continue
    
    loc = bisect_left(stack, num)
    stack[loc] = num
    
print(len(stack))