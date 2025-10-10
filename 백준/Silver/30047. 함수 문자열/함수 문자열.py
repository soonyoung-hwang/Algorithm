import sys

input = sys.stdin.readline
string_list = list(input().rstrip())

answer = 0
stack = []
for i in range(len(string_list) - 1, -1, -1):
    if string_list[i] == "x":
        stack.append(0)
    if string_list[i] == "g":
        if not stack:
            answer = -1
            break
        temp = stack.pop()
        stack.append(temp + 1)
    if string_list[i] == "f":
        if len(stack) < 2:
            stack = []
            answer = -1
            break
        temp1 = stack.pop()
        temp2 = stack.pop()
        stack.append(min(temp1, temp2))

if len(stack) != 1:
    answer = -1
else:
    answer = stack.pop()

print(answer)