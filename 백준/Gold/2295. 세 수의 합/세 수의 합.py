N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

plus = set()

for i in range(N - 1):
    for j in range(i, N - 1):
        plus.add(numbers[i] + numbers[j])

answer = -1
for i in range(N - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if (numbers[i] - numbers[j]) in plus:
            answer = numbers[i]
            break

    if answer != -1:
        break

print(answer)
