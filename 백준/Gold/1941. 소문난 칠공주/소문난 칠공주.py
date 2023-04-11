board = [list(input().rstrip()) for _ in range(5)]

dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer = 0
dasom = 0
doyeon = 0

def check():
    visited = [[False for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if board[i][j] == True:
                stack = []
                cnt = 0

                stack.append((i, j))
                visited[i][j] = True
                while stack:
                    cnt += 1
                    r, c = stack.pop()
                
                    for k in range(4):
                        nr, nc = r + dd[k][0], c + dd[k][1]
                        if not (0<= nr < 5 and 0<= nc < 5): continue
                        if not (board[nr][nc] == True): continue
                        if visited[nr][nc] : continue
                        visited[nr][nc] = True
                        stack.append((nr, nc))

                if cnt != 7:
                    return False

                else:
                    return True                    
                


def dfs(idx, dasom, doyeon):
    global answer
    if doyeon >= 4:
        return

    if doyeon + dasom == 7:
        if check():
            answer += 1
        return
    
    
    for i in range(idx, 25):
        r, c = i // 5, i % 5
        temp = board[r][c]
        board[r][c] = True
        if temp == 'Y':
            dfs(i+1, dasom, doyeon+1)
        else:
            dfs(i+1, dasom+1, doyeon)
        board[r][c] = temp


    

dfs(0, 0, 0)
print(answer)