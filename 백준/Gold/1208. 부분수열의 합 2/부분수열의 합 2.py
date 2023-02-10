# 부분수열의 합 2
# 정수의 갯수 N <= 40
# 2^40 = (2^10)^4 = 1000000000000

# 절반으로 나눠서 모든 부분집합의 합을 구하고
# 2^20 + 2^20 // 정렬 후 이분탐색을 통해, 답을 구한다.
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))

if N == 1:
    if arr[0] == M:
        print(1)
    else:
        print(0)

    exit(0)

arr.sort()

left_groups = []
right_groups = []
def backtracking(s, sum, e, group):
    if s == e:
        group.append(sum+arr[s])       # index s is included
        group.append(sum)              # index s is not included
        return
    
    backtracking(s+1, sum+arr[s], e, group)    # index s is included
    backtracking(s+1, sum, e, group)           # index s is not included

backtracking(0, 0, N//2-1, left_groups)
backtracking(N//2, 0, N-1, right_groups)

left_groups.sort()
right_groups.sort(reverse=True)

start_l, start_r = 0, 0

count = 0
while start_l < len(left_groups) and start_r < len(right_groups):
    tmp = left_groups[start_l]+right_groups[start_r]
    if tmp == M:
        count_l = 1
        count_r = 1
        while start_l < len(left_groups)-1 and left_groups[start_l] == left_groups[start_l+1]:
            count_l += 1
            start_l += 1
        
        while start_r < len(right_groups)-1 and right_groups[start_r] == right_groups[start_r+1]:
            count_r += 1
            start_r += 1
        
        count += count_l * count_r
        
        start_l += 1
        start_r += 1
    
    elif tmp < M:
        start_l += 1
    
    else:
        start_r += 1

if M == 0 and count > 0:
    print(count-1)
else:
    print(count)