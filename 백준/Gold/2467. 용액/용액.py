N = int(input())
number = list(map(int,input().split()))

current = 2_000_000_001
answer = [-1, -1]

l, r = 0, N-1
while l < r:
    if abs(number[l] + number[r]) < abs(current):
        current = number[l] + number[r]
        answer = [number[l], number[r]]
    
    if number[l] + number[r] == 0:
        break
    elif number[l] + number[r] > 0:
        r -= 1
    else:
        l += 1

print(*answer)