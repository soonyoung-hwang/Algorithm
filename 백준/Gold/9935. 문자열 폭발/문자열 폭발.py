import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = list(input().rstrip())

lb = len(bomb) # length_bomb

stack = []
for i in range(len(s)):
    stack.append(s[i])
    ls = len(stack)
    if len(stack) >= lb and stack[-lb:] == bomb:
        for j in range(lb):
            stack.pop()

print("".join(stack) if stack else "FRULA")