import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def num_to_coordinates(num):
    return num//N, num%N

def coordinates_to_num(H,W):
    return N*H+W

candidates = []
visited = [False for _ in range(N*N)]
evens = []
odds = []
for i in range(N):
    for j in range(N):
        if board[i][j]:
            candidates.append(coordinates_to_num(i, j))
            if (i+j)%2 == 0:
                evens.append(coordinates_to_num(i, j))
            else:
                odds.append(coordinates_to_num(i, j))
        else:
            visited[coordinates_to_num(i, j)] = True

L = len(candidates)

# 전처리 : 미리 상극인 것들 구해놓는다.
skip = defaultdict(list)
for c1 in candidates:
    for c2 in candidates:
        if c1 >= c2:
            continue
        h1, w1 = num_to_coordinates(c1)
        h2, w2 = num_to_coordinates(c2)
        if abs(h1-h2) == abs(w1-w2):
            skip[c1].append(c2)
        
max_count = 0
def backtracking(idx, count, list_to_explore):
    global max_count
    
    # idx가 포함 안 되어있을 때,
    for i in list_to_explore:
        if i <= idx:
            continue
        if not visited[i]:
            backtracking(i, count, list_to_explore)
            break

    # idx가 포함되었을 때, idx로 인해, 못 들어오는 것들 계산
    if visited[idx]:
        return

    max_count = max(max_count, count+1) # idx들어 왔을 때, max count 갱신
    killed = []
    for i in list_to_explore:
        if i <= idx:
            continue
        if visited[i]:
            continue
        if i in skip[idx]:
            killed.append(i)
            visited[i] = True
    
    # 못 들어오는 것들 빼고, 하나씩 들어오게 한다.
    for i in list_to_explore:
        if i <= idx:
            continue
        if not visited[i]:
            backtracking(i, count+1, list_to_explore)
            break
    
    # idx에 의해 제거된 것들 복구
    for k in killed:
        visited[k] = False


answer = 0

max_count = 0
backtracking(0, 0, evens)
answer += max_count

max_count = 0
backtracking(1, 0, odds)
answer += max_count

print(answer)