import sys

N = int(sys.stdin.readline().rstrip())
max_dp = [0 for __ in range(3)]
min_dp = [0 for __ in range(3)]
max_temp = [0 for __ in range(3)]
min_temp = [0 for __ in range(3)]
d = (-1, 0, 1)

for __ in range(N):
    arr = list(map(int,sys.stdin.readline().split()))
    for i in range(3):
        max_previous = 0
        min_previous = 900000
        for j in range(3):
            ni = i+d[j]
            if 0 <= ni < 3:
                max_previous = max(max_previous, max_dp[ni])
                min_previous = min(min_previous, min_dp[ni])
                
        max_temp[i] = arr[i] + max_previous
        min_temp[i] = arr[i] + min_previous
                
    for i in range(3):
        max_dp[i] = max_temp[i]
        min_dp[i] = min_temp[i]
        
print(max(max_dp), min(min_dp))