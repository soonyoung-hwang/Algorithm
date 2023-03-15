import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
score = 0
blocks = 0
board = [[deque([False for __ in range(6)]) for __ in range(4)], [deque([False for __ in range(6)]) for __ in range(4)]] # blue/ green


def BtoG(t, x, y):
    if t == 1: t = 1
    elif t == 2: t = 3
    elif t == 3: t = 2

    x, y = 3-y, x
    if t == 3:
        x -= 1
    return t, x, y

def board_update(color, t, r, c):
    if t == 2:
        start = 0
        while start < 5 and board[color][r][start+1] == False:
            start += 1

        board[color][r][start] = True
        board[color][r][start-1] = True
    
    elif t == 3:
        start = 0
        while start < 5 and board[color][r][start+1] == False and board[color][r+1][start+1] == False:
            start += 1
        
        board[color][r][start] = True
        board[color][r+1][start] = True


    elif t == 1:
        start = 0
        while start < 5 and board[color][r][start+1] == False:
            start += 1
        
        board[color][r][start] = True
    
def process():
    global score
    for bd in board:
        for i in range(1,6,1):    # column
            to_remove = True
            for j in range(4):    # row
                if bd[j][i] == False:
                    to_remove = False
                    break
            
            if to_remove:
                score += 1
                for j in range(4):
                    del bd[j][i]
                    bd[j].appendleft(False)
        

        num_to_remove = 0
        for i in range(1, -1, -1):
            to_remove = False
            for j in range(0,4):    # row
                if bd[j][i] == True:
                    to_remove = True
                    break

            if to_remove:
                num_to_remove += 1
        
        for i in range(num_to_remove):
            for j in range(4):
                bd[j].pop()
                bd[j].appendleft(False)



for __ in range(N):
    t, r, c = map(int,input().split())
    # calculate blue
    board_update(0, t, r, c)
    t, r, c = BtoG(t, r, c)
    board_update(1, t, r, c)
    # calculate green
    process()
    
for bd in board:
    for i in range(6):
        for j in range(4):
            if bd[j][i] == True:
                blocks += 1
print(score)
print(blocks)