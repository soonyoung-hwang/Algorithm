import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

# 1. 전처리
N, M = map(int,input().split())
board = [list(map(int,input().split())) for __ in range(N)]
blizzard = [tuple(map(int,input().split())) for __ in range(M)]


dd = ((0, -1), (1, 0), (0, 1), (-1, 0))
num2rc = defaultdict(tuple)
rc2num = defaultdict(int)
num_value = defaultdict(int)

rc2num[(N//2, N//2)] = 0
num2rc[0] = (N//2, N//2)
answer = 0

# 2. 자료구조 1, 2 만들기
cur = (N//2, N//2)
cur_dir = 0
name = 1
for i in range(1,N+1):
    if i != N:
        for j in range(2):
            for k in range(i):
                r, c = cur
                nr, nc = r+dd[cur_dir][0], c+dd[cur_dir][1]
                num2rc[name] = (nr, nc)
                rc2num[(nr, nc)] = name
                
                cur = (nr, nc)
                name += 1

            cur_dir = (cur_dir+1)%4
    else:
        for k in range(i-1):
            r, c = cur
            nr, nc = r+dd[cur_dir][0], c+dd[cur_dir][1]
            num2rc[name] = (nr, nc)
            rc2num[(nr, nc)] = name
            cur = (nr, nc)
            name += 1

# 3. 자료구조 3 만들기
for i in range(N):
    for j in range(N):
        num_value[rc2num[(i,j)]] = board[i][j]


# 구슬파괴
meteo_direction = ((-1,0), (1,0), (0,-1), (0,1))
def casting(d, s):
    temp_d = meteo_direction[d-1]
    r, c = N//2, N//2
    for i in range(1,s+1):
        nr, nc = r + temp_d[0]*i, c + temp_d[1]*i
        
        num_value[rc2num[(nr, nc)]] = 0
        board[nr][nc] = 0


# 구슬 이동 and 구슬 폭발 and 구슬 증폭
def move_and_explore():
    global answer
    # 구슬 이동 + 폭발
    temp = deque()
    for i in range(1,N*N):
        if num_value[i]:
            temp.append(num_value[i])

    added = 1
    while added:
        added = 0
        new_temp = []
        
        while temp:
            q = temp.popleft()
            temp_count = 1
            while temp and temp[0] == q:
                temp.popleft()
                temp_count += 1
            
            if temp_count >= 4:
                added += temp_count * q
            
            else:
                for i in range(temp_count):
                    new_temp.append(q)
        
        answer += added
        temp = deque(new_temp[:])

    # 구슬 증폭
    new_array = deque()
    while temp:
        q = temp.popleft()
        temp_count = 1
        while temp and temp[0] == q:
            temp.popleft()
            temp_count += 1
        new_array.append(temp_count)
        new_array.append(q)
    
    
    while len(new_array) > N*N-1:
        new_array.pop()
    
    
    for i in range(N):
        for j in range(N):
            board[i][j] = 0

    i = 1
    while new_array:
        r, c = num2rc[i]
        board[r][c] = new_array.popleft()
        i += 1


    for i in range(N):
        for j in range(N):
            num_value[rc2num[(i,j)]] = board[i][j]

# 실행
answer = 0

for b in blizzard:
    d, s = b
    casting(d,s)    
    move_and_explore()
    
print(answer)