import sys
input = sys.stdin.readline

# initialize
def segmentize(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start+end)//2
    tree[index] = segmentize(start, mid, index*2) + segmentize(mid+1, end, index*2+1)
    return tree[index]

def find(start, end, lidx, ridx, loc):
    
    if start > ridx or end < lidx: # 겹치는 구간 없으면 0 리턴
        return 0
        
    # 1. 해당 노드가 구하는 인덱스 안에 포함 될 때 -> 리턴 하면 된다.
    if start <= lidx and end >= ridx:
        return tree[loc]
    
    # 2. 뭔가 쪼개질 때 반 반 줄인다.
    mid = (lidx + ridx)//2
    l_lidx, l_ridx, l_loc = lidx, mid, loc*2
    r_lidx, r_ridx, r_loc = mid+1, ridx, loc*2+1
    return find(start, end, l_lidx, l_ridx, l_loc) + find(start, end, r_lidx, r_ridx, r_loc)

def visualize_tree():
    c = 1
    for i in range(1,4*n):
        if i % (2*c) == 0:
            print("")
            c *= 2
        print(tree[i], end=' ')
    print("\n")
    
def query_2(b,c):
    print(find(b,c,1,n,1))

def replace(index, value, lidx, ridx, loc):
    if lidx <= index and index <= ridx:
        tree[loc] -= arr[index]
        tree[loc] += value
        
    else:
        return
    
    if lidx == ridx:
        return
    
    mid = (lidx + ridx)//2
    l_lidx, l_ridx, l_loc = lidx, mid, loc*2
    r_lidx, r_ridx, r_loc = mid+1, ridx, loc*2+1
    
    replace(index, value, l_lidx, l_ridx, l_loc)
    replace(index, value, r_lidx, r_ridx, r_loc)

    
def query_1(b,c):
    replace(b, c, 1, n, 1)
    arr[b] = c
    
    
n, m, k = map(int,input().split())
arr = [0] + [int(input()) for __ in range(n)]
tree = [0]*(4*n)        
segmentize(1, n, 1) # init

for __ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        query_1(b,c)
    elif a == 2:
        query_2(b,c)