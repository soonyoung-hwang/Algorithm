# 백준 19236: 청소년상어

# dfs 방식으로 모든 경우의 수 찾아가기.. 앞에 숫자가 없어지면 끝

from copy import deepcopy

board = []
fish = [[] for __ in range(17)]
for i in range(4):
    a, ad, b, bd, c, cd, d, dd = map(int,input().split())
    board.append([[a], [b], [c], [d]])
    fish[a].extend([i, 0, ad, False])   # fish[a] : a번 물고기의 [r, c, 먹혔는지 상태]
    fish[b].extend([i, 1, bd, False])
    fish[c].extend([i, 2, cd, False])
    fish[d].extend([i, 3, dd, False])

answer = 0
direction = ((-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0, 1),(-1,1))

def commit_fish(s_r, s_c):
    for i in range(1,17):
        f = fish[i]
        if f[3]:    # if fish died, then ignore it
            continue
        
        # 살아있는 고기 -> board[r][c]에는 고기가 무조건 존재 해야한다.
        r, c, d = f[0], f[1], f[2]
        
        nr, nc = r+direction[d-1][0], c+direction[d-1][1]
        while (not (0<=nr<4 and 0<=nc<4)) or (nr == s_r and nc == s_c): # 길이 있을 때 까지 회전
            d = (d+1)%8
            nr, nc = r+direction[d-1][0], c+direction[d-1][1]
        
        if not board[nr][nc]:   # 가는 곳이 빈칸이면
            board[nr][nc].append(i)
            board[r][c].pop()
            fish[i][0], fish[i][1], fish[i][2] = nr, nc, d
        
        else:
            origin = board[nr][nc].pop()
            board[r][c].pop()
            board[r][c].append(origin)
            board[nr][nc].append(i)
            fish[i][0], fish[i][1], fish[i][2] = nr, nc, d
            fish[origin][0], fish[origin][1] = r, c
    



def shark_next(r, c, d):
    candi = []
    for i in range(1,5):
        nr, nc = r+direction[d-1][0]*i, c+direction[d-1][1]*i
        if (0<=nr<4 and 0<=nc<4) and board[nr][nc]:
            candi.append([nr,nc])
    return candi


def dfs(r, c, d, score):
    global answer
    global board
    global fish
    # r c is location of the shark and d is direction
    # score is current score

    # 물고기 움직인다
    temp_board = deepcopy(board)
    temp_fish = deepcopy(fish)

    commit_fish(r, c)

    moved_board = deepcopy(board)
    moved_fish = deepcopy(fish)

    # 상어 다음 행동
    nexts = shark_next(r, c, d)
    
    if not nexts:
        answer = max(answer, score)
        board = deepcopy(temp_board)
        fish = deepcopy(temp_fish)
        return

    for rr, cc in nexts:
        board = deepcopy(moved_board)
        fish = deepcopy(moved_fish)

        f = board[rr][cc].pop()   # f : rr cc에 있는 물고기의 번호

        # f를 잡아먹은 상태
        new_score = score + f
        nd = fish[f][2]
        fish[f][3] = True
        dfs(rr, cc, nd, new_score)
        # board가 망가진다.

        
        # 복구
        board[rr][cc].append(f)
        fish[f][3] = False

    # 물고기 원상복구
    board = deepcopy(temp_board)
    fish = deepcopy(temp_fish)
    return


first_gogi = board[0][0].pop()
fish[first_gogi][3] = True
first_d = fish[first_gogi][2]
dfs(0, 0, first_d, first_gogi)



print(answer)