import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
board = [input().rstrip() for _ in range(N)]

answer = 4_000_000

# case 1. 왼 위 white
temp = [[] for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(M):
        if (i+j)%2 == 0 and board[i][j] != 'W':
            cnt += 1
        elif (i+j)%2 == 1 and board[i][j] == 'W':
            cnt += 1
    
        if j >= K:
            if (i+(j-K))%2 == 0 and board[i][j-K] != 'W':
                cnt -= 1
            elif (i+(j-K))%2 == 1 and board[i][j-K] == 'W':
                cnt -= 1
        
        if j >= K-1:
            temp[i].append(cnt)


for j in range(M-K+1):
    cnt = 0
    for i in range(N):
        cnt += temp[i][j]

        if i >= K:
            cnt -= temp[i-K][j]

        if i >= K-1:
            answer = min(answer, cnt)
            # temp2[j].append(cnt)

# case 2. 왼 위 black
temp = [[] for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(M):
        if (i+j)%2 == 0 and board[i][j] != 'B':
            cnt += 1
        elif (i+j)%2 == 1 and board[i][j] == 'B':
            cnt += 1
    
        if j >= K:
            if (i+(j-K))%2 == 0 and board[i][j-K] != 'B':
                cnt -= 1
            elif (i+(j-K))%2 == 1 and board[i][j-K] == 'B':
                cnt -= 1

        if j >= K-1:
            temp[i].append(cnt)

for j in range(M-K+1):
    cnt = 0
    for i in range(N):
        cnt += temp[i][j]

        if i >= K:
            cnt -= temp[i-K][j]

        if i >= K-1:
            answer = min(answer, cnt)

print(answer)