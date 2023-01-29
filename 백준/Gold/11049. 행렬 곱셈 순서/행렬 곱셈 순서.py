import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,input().split())) for __ in range(N)]
arr = [[2**31 for i in range(N)] for __ in range(N)]

for i in range(N):
    for j in range(N-i):
        if i == 0:
            arr[j][j+i] = 0
            continue
        

        for k in range(i):
            arr[j][j+i] = min(arr[j][j+i], \
                arr[j][j+k]+arr[j+1+k][j+i]+matrix[j][0]*matrix[j+1+k][0]*matrix[j+i][1])

print(arr[0][-1])