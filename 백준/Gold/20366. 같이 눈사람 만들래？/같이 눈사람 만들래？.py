import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = sys.maxsize

for i in range(N):
    for j in range(N-1, i+2, -1):
        num1 = arr[i] + arr[j]
        left, right = i+1, j-1
        
        while left < right:
            num2 = arr[left] + arr[right]
            result = min(result,abs(num1-num2))
            if num2 > num1:
                right -=1
            else:
                left += 1
print(result)