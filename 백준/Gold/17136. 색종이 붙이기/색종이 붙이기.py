import sys
input = sys.stdin.readline
from copy import deepcopy

arr = [list(map(int,input().split())) for __ in range(10)]

def cover_with_paper(ii,jj,size):
    for i in range(ii,ii+size):
        for j in range(jj,jj+size):
            arr[i][j] ^= 1


def find_length(ii,jj):
    size = 5
    while size > 1:
        found = True
        for i in range(size):
            for j in range(size):
                if ii+i >= 10 or jj+j >= 10:
                    found = False
                    break
                if arr[ii+i][jj+j] == 0:
                    found = False
        if found:
            break
    
        size -= 1
    
    return size

answer = 26

total = 0
for i in range(10):
    total += sum(arr[i])

all_poss = []
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    if i*1+j*4+k*9+l*16+m*25 == total:
                        all_poss.append([i,j,k,l,m])

all_poss.sort(key=lambda x:sum(x))

def dfs(total_used):
    global answer

    is_all_zero = True
    for i in range(10):
        if sum(arr[i]) != 0:
            is_all_zero = False
    
    if is_all_zero:
        answer = min(answer,total_used)
        return 

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                L = find_length(i,j)
                dfs_in = False
                for size in range(L,0,-1):
                    if papers[size-1]:
                        papers[size-1] -= 1
                        cover_with_paper(i,j,size)
                        dfs(total_used+1)
                        papers[size-1] += 1
                        cover_with_paper(i,j,size)
                        dfs_in=True

                return

for poss in all_poss:
    papers = poss
    dfs(0)
    if answer != 26:
        break

print(answer if answer != 26 else -1)
    