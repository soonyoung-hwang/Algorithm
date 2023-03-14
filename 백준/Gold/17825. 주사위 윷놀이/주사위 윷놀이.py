answer = 0
dices = [0,0,0,0]
def dfs(score, idx):
    global answer
    if idx == 10:
        answer = max(answer, score)
        return

    for i in range(4):
        move = orders[idx]
        add = 0
        # move dice
        temp_next = dices[i]
        origin = temp_next
        if origin == 50:
            continue

        if origin in (5,10,15):
            if move == 1:
                add += routes[temp_next][1][1]
            temp_next = routes[temp_next][1][0]
            move -= 1

        for m in range(move):
            if type(routes[temp_next]) == list:
                if m == move-1:
                    add += routes[temp_next][0][1]
                temp_next = routes[temp_next][0][0]
                
            else:
                if m == move-1:
                    add += routes[temp_next][1]
                temp_next = routes[temp_next][0]

            if temp_next == 50:
                break


        if temp_next != 50 and temp_next in dices:
            continue

        dices[i] = temp_next
        dfs(score+add, idx+1)
        dices[i] = origin


orders = list(map(int,input().split()))
routes = {0:(1,2), 1:(2,4), 2:(3,6), 3:(4,8), 4:(5,10), 5:[(6,12),(21,13)], \
    6:(7,14), 7:(8,16), 8:(9,18), 9:(10,20), 10:[(11,22),(31,22)], \
        11:(12,24), 12:(13,26), 13:(14,28), 14:(15,30), 15:[(16,32),(41,28)], \
            16:(17, 34), 17:(18,36), 18:(19,38), 19:(20, 40), 20:(50, 0), \
                21:(22, 16), 22:(23, 19), 23:(24, 25), 24:(25, 30), 25:(26, 35), \
                    26:(20,40), 31:(32, 24), 32:(24, 25), 41:(42, 27), 42:(43, 26), 43:(24, 25), \
                        }


dfs(0, 0)
print(answer)