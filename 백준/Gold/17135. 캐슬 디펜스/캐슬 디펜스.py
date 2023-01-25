# 캐슬디펜스

from collections import deque
from copy import deepcopy

N, M, D = map(int,input().split())
arr_origin = deque([list(map(int,input().split())) for __ in range(N)])

_dir = ((0, -1),(-1, 0), (0, 1))

def calculate():
    global D

    score = 0
    prior = dict()
    for archer in stack:
        prior[archer] = []

        Q = deque([[[N-1,archer], 1]])
        
        visited = [[False for __ in range(M)] for __ in range(N)]
        visited[N-1][archer] = True
        prior[archer].append([N-1, archer])

        while Q:
            q, distance = Q.popleft()
            if distance == D:
                break
            prior[archer].append(q[:])
            for dd in _dir:
                nc, nr = q[0]+dd[0], q[1]+dd[1]
                if not (0 <= nc < N and 0 <= nr < M):
                    continue
                if visited[nc][nr]:
                    continue
                visited[nc][nr] = True
                prior[archer].append([nc,nr])
                Q.append([[nc, nr], distance+1])
    
    score = 0
    arr = deepcopy(arr_origin)
    for i in range(N+1):
        killed = []
        for archer in stack:
            for sc, sr in (prior[archer]):
                if arr[sc][sr]:
                    if [sc, sr] not in killed:
                        killed.append([sc,sr])
                    break

        score += len(killed)
        for dc,dr in killed:
            arr[dc][dr] = 0

        arr.pop()
        arr.appendleft([0 for __ in range(M)])

    return score

stack = []
def dfs(idx):
    global total
    if(len(stack) == 3):
        score = calculate()
        total = max(total, score)
        return
    
    if idx > M-1:
        return

    stack.append(idx)
    dfs(idx+1)
    stack.pop()
    dfs(idx+1)

total = 0
dfs(0)
print(total)