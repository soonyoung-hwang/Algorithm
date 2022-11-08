N, M, x, y, K = map(int,input().split())
maps = []
ops = []
for _ in range(N):
    maps.append(list(map(int,input().split())))
ops = list(map(int,input().split()))

dice = [[0, 0, 0], [0, 0, 0, 0]]
# 0 0 0 : 서, 위 , 동
# 0 0 0 0 : 북, 위, 남, 밑
# dice[0][1] always should keep equal to dice[1][1]
# 밑 = dice[1][3]
# op : [1, 2, 3, 4]  = [동, 서, 북, 남]

# dice = [[4, 1, 3], [2,1,5,6]]
before_dice = [[0, 0, 0], [0, 0, 0, 0]]
for i in range(K):
    op = ops[i]
    if(op == 4):
        x += 1
        if(x >= N):
            x -= 1
            continue
            
        dice[0][1] = dice[1][0]
        dice[1][0], dice[1][1], dice[1][2], dice[1][3] = dice[1][3], dice[1][0], dice[1][1], dice[1][2]            
            
    elif(op == 3):
        x -= 1
        if(x < 0):
            x += 1
            continue
            
        dice[0][1] = dice[1][2]
        dice[1][0], dice[1][1], dice[1][2], dice[1][3] = dice[1][1], dice[1][2], dice[1][3], dice[1][0]
        
    elif(op == 1):
        y += 1
        if(y >= M):
            y -= 1
            continue
            
        before_dice[0] = dice[0][:]
        before_dice[1] = dice[1][:]
        dice[0][0], dice[0][1], dice[0][2] = dice[1][3], dice[0][0], dice[0][1]
        dice[1][1], dice[1][3] = before_dice[0][0], before_dice[0][2]

    elif(op == 2):
        y -= 1
        if(y < 0):
            y += 1
            continue
            
        before_dice[0] = dice[0][:]
        before_dice[1] = dice[1][:]
        dice[0][0], dice[0][1], dice[0][2] = dice[0][1], dice[0][2], dice[1][3]
        dice[1][1], dice[1][3] = before_dice[0][2], before_dice[0][0]

    if(maps[x][y] == 0):
        maps[x][y] = dice[1][3]
    else:
        dice[1][3], maps[x][y] = maps[x][y], 0
        
    print(dice[0][1])

