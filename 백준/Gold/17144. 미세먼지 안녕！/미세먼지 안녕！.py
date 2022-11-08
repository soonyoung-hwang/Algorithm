def spread():
    changes = [[0]*C for __ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] < 5:
                continue
            amount_to_spread = arr[i][j] // 5
            nums_to_spread = 0
            if i-1 >= 0 and arr[i-1][j] != -1:
                nums_to_spread += 1
                changes[i-1][j] += amount_to_spread
            if i+1 < R and arr[i+1][j] != -1:
                nums_to_spread += 1
                changes[i+1][j] += amount_to_spread
            if j-1 >= 0 and arr[i][j-1] != -1:
                nums_to_spread += 1
                changes[i][j-1] += amount_to_spread
            if j+1 < C and arr[i][j+1] != -1:
                nums_to_spread += 1
                changes[i][j+1] += amount_to_spread
               
            changes[i][j] -= (nums_to_spread*amount_to_spread)
    
    for i in range(R):
        for j in range(C):
            arr[i][j] += changes[i][j]
    
def circulation():    
    # up
    # 1 - 아래
    temp = arr[up][C - 1]
    for i in range(C - 1, 1, - 1):
        arr[up][i] = arr[up][i - 1]
    arr[up][1] = 0

    # 2 - 오른쪽
    temp_1 = arr[0][C - 1]
    for i in range(up - 1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    arr[up - 1][C - 1] = temp

    # 3 - 위쪽
    temp_2 = arr[0][0]
    for i in range(C - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(up - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2

    # down
    # 1- 위쪽
    temp = arr[down][C - 1]
    for i in range(C - 1, 1, -1):
        arr[down][i] = arr[down][i - 1]
    arr[down][1] = 0

    # 2 오른쪽
    temp_1 = arr[R - 1][C - 1]
    for i in range(R - 1, down + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    arr[down + 1][C - 1] = temp

    # 3 - 아래쪽
    temp_2 = arr[R - 1][0]
    for i in range(C - 2):
        arr[R - 1][i] = arr[R - 1][i + 1]
    arr[R - 1][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(down + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[R - 2][0] = temp_2
    
    
R, C, T = map(int,input().split())
arr = [list(map(int,input().split())) for __ in range(R)]

loc_purifier = []
for i in range(R):
    if arr[i][0] == -1:
        loc_purifier.append(i)

up, down = loc_purifier
for __ in range(T):
    spread()
    circulation()


ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)