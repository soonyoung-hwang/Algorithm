import sys
input = sys.stdin.readline

for __ in range(int(input())):
    n = int(input())
    numbers = []
    for __ in range(n):
        numbers.append(input().rstrip())
    numbers.sort(reverse=True)
    
    flag = True
    for i in range(1,n):
        if numbers[i-1].startswith(numbers[i]):
            flag = False
            break

    print("YES" if flag else "NO")