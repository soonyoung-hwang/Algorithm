import sys
sys.setrecursionlimit(10**6)

N = int(input())
ino = list(map(int,input().split()))
posto = list(map(int,input().split()))

answer = []

index = [0] * (N+1)
for i in range(N):
    index[ino[i]] = i

answer = []

def preo(i_start, i_end, p_start, p_end):
    if(i_start > i_end):
        return
    
    root = posto[p_end]
    answer.append(root)
    
    idx = index[root]
    left = idx-i_start
    right = i_end-idx
    
    preo(i_start, i_start+left-1, p_start, p_start+left-1)
    preo(i_end-right+1, i_end, p_end-right,p_end-1)

preo(0,N-1,0,N-1)
print(*answer)
    