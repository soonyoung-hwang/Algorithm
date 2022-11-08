from collections import deque
import sys

d = ((0,1), (0,-1), (-1,0), (1,0))


def inrange(i,j):
    return (0 <= i <= n-1) and (0 <= j <= n-1)

def find_neighbour(arr,i,j,group_array):
    flag = group_array[i][j]
    
    Q = deque([[i,j]])
    
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if not inrange(nx,ny):
                continue
            if group_array[nx][ny] != 0:
                continue
            if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                group_array[nx][ny] = flag
                Q.append([nx,ny])

    return

def find_group(arr):
    n = len(arr)
    group_array = [[0]*n for __ in range(n)]
    
    flag = 1
    for i in range(n):
        for j in range(n):
            if(group_array[i][j] == 0):
                group_array[i][j] = flag
                find_neighbour(arr,i,j,group_array)                    
                flag += 1
                
    return [group_array, flag-1]

def update(arr, group_array, num_of_groups):
    totals = [0]*(num_of_groups+1)
    nums = [0]*(num_of_groups+1)
    
    
    for i in range(n):
        for j in range(n):
            nums[group_array[i][j]] += 1
            totals[group_array[i][j]] += arr[i][j]
    
    for i in range(1,num_of_groups+1):
        totals[i] //= nums[i]
        
    for i in range(n):
        for j in range(n):
            arr[i][j] = totals[group_array[i][j]]

            
n, L, R = map(int,sys.stdin.readline().rstrip().split())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for __ in range(n)]            


ans = 0
while True:
    groups, num_of_groups = find_group(arr)    
    if num_of_groups == n*n:
        break

    update(arr,groups,num_of_groups)
        
    ans += 1
    
print(ans)
