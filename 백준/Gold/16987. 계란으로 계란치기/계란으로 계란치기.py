
N = int(input())
eggs = [list(map(int,input().split())) for _ in range(N)]

answer = 0

def dfs(idx, count):
    global answer
    if idx == N:
        # 10초밖에 안 걸려
        answer = max(answer, count)
        return
    
    if eggs[idx][0] > 0:
        fight = False
        for i in range(N):
            if idx == i:
                continue
            if eggs[i][0] <= 0:
                continue
            
            idx_durability = eggs[idx][0]
            target_durability = eggs[i][0]

            eggs[idx][0], eggs[i][0] = eggs[idx][0] - eggs[i][1], eggs[i][0] - eggs[idx][1]
            add = 0
            if eggs[idx][0] <= 0:
                add += 1
            if eggs[i][0] <= 0:
                add += 1
            
            dfs(idx+1, count+add)
            eggs[idx][0], eggs[i][0] = idx_durability, target_durability
            fight = True

        if not fight:
            dfs(idx+1, count)
            
        
    else:
        dfs(idx+1, count)

dfs(0, 0)
print(answer)