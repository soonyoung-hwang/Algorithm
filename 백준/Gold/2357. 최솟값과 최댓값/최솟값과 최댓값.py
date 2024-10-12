import sys

input = sys.stdin.readline
MAX = sys.maxsize
MIN = -sys.maxsize


def init_min(idx, left, right):
    if left == right:
        tree_min[idx] = arr[left]
        return tree_min[idx]

    mid = (left + right) // 2
    leftVal = init_min(idx * 2, left, mid)
    rightVal = init_min(idx * 2 + 1, mid + 1, right)
    tree_min[idx] = min(leftVal, rightVal)

    return tree_min[idx]


def init_max(idx, left, right):
    if left == right:
        tree_max[idx] = arr[left]
        return tree_max[idx]

    mid = (left + right) // 2
    leftVal = init_max(idx * 2, left, mid)
    rightVal = init_max(idx * 2 + 1, mid + 1, right)
    tree_max[idx] = max(leftVal, rightVal)

    return tree_max[idx]


def query_min(idx, fr, to, left, right):
    if fr <= left and right <= to:
        return tree_min[idx]

    if right < fr or to < left:
        return MAX

    mid = (left + right) // 2
    leftVal = query_min(idx * 2, fr, to, left, mid)
    rightVal = query_min(idx * 2 + 1, fr, to, mid + 1, right)
    return min(leftVal, rightVal)


def query_max(idx, fr, to, left, right):
    if fr <= left and right <= to:
        return tree_max[idx]

    if right < fr or to < left:
        return MIN

    mid = (left + right) // 2
    leftVal = query_max(idx * 2, fr, to, left, mid)
    rightVal = query_max(idx * 2 + 1, fr, to, mid + 1, right)
    return max(leftVal, rightVal)



N, M = map(int, input().split())
arr = [0] + [int(input().strip()) for _ in range(N)]
tree_min = [MAX for _ in range(4 * N)]
tree_max = [MIN for _ in range(4 * N)]

init_min(1, 1, N)
init_max(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    print(" ".join([str(query_min(1, a, b, 1, N)), str(query_max(1, a, b, 1, N))]))
