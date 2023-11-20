import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())
numbers = [0] + list(map(int,input().split()))
max_size = 2**math.ceil(math.log2(N))
segment_tree = [0 for _ in range(max_size*2)]


def initialize2(i, left, right):
    if left == right:
        segment_tree[i] = numbers[left]
        return segment_tree[i]
    
    mid = (left + right)//2
    segment_tree[i] = initialize2(i*2, left, mid) + initialize2(i*2+1, mid+1, right)
    return segment_tree[i]

initialize2(1, 1, N)


def find2(start, end, target_start, target_end, i):
    if end < target_start or start > target_end:
        return 0
    
    if target_start <= start and end <= target_end:
        return segment_tree[i]
    
    mid = (start + end) // 2
    return find2(start, mid, target_start, target_end, i*2) + find2(mid+1, end, target_start, target_end, i*2+1)
        
def edit(idx, th, diff, start, end):
    if th < start or th > end:
        return

    segment_tree[idx] += diff
    mid = (start + end) // 2
    if start==end:
        numbers[start] += diff
        return

    edit(idx*2, th, diff, start, mid)
    edit(idx*2+1, th, diff, mid+1, end)
    return
    

for _ in range(M):
    x, y, idx, num = list(map(int,input().split()))
    if x > y:
        y, x = x, y

    print(find2(1, N, x, y, 1))
    diff = num - numbers[idx]
    edit(1, idx, diff, 1, N)
