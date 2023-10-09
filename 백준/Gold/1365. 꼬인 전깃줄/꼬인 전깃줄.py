from bisect import bisect

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

stack = []
for number in numbers:
    if not stack or stack[-1] < number:
        stack.append(number)
        continue

    loc = bisect(stack, number)
    stack[loc] = number

print(N - len(stack))
