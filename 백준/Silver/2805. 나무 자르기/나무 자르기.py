import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int,input().split()))

def is_possible(num):
    res = 0
    for tree in trees:
        res += max(0, tree-num)
        
    if res >= M:
        return True
    return False

l, r = 0, 1000000001

while l < r:
    m = (l+r)//2
    if is_possible(m):
        l = m+1
    else:
        r = m

print(l-1)