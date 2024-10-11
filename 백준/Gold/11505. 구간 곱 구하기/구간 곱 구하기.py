import sys

input = sys.stdin.readline

MOD = 1_000_000_007


def init(idx, left, right):
    if left == right:
        tree[idx] = arr[left]
        return tree[idx]

    mid = (left + right) // 2
    leftVal = init(idx * 2, left, mid)
    rightVal = init(idx * 2 + 1, mid + 1, right)
    tree[idx] = (leftVal * rightVal) % MOD

    return tree[idx]


def query(idx, fr, to, left, right):
    if fr <= left and right <= to:
        return tree[idx]

    if right < fr or to < left:
        return 1

    mid = (left + right) // 2
    leftVal = query(idx * 2, fr, to, left, mid)
    rightVal = query(idx * 2 + 1, fr, to, mid + 1, right)
    return (leftVal * rightVal) % MOD


def update(idx, loc, val, left, right):
    if not (left <= loc <= right):
        return tree[idx]

    # loc을 포함하는 노드들
    if left == right:
        tree[idx] = val
        return tree[idx]

    mid = (left + right) // 2
    leftVal = update(idx * 2, loc, val, left, mid)
    rightVal = update(idx * 2 + 1, loc, val, mid + 1, right)
    tree[idx] = (leftVal * rightVal) % MOD

    return tree[idx]


N, M, K = map(int, input().split())
arr = [0] + [int(input().strip()) for _ in range(N)]
tree = [1 for _ in range(4 * N)]

init(1, 1, N)
for _ in range(M + K):

    a, b, c = map(int, input().split())
    if a == 1:  # change
        update(1, b, c, 1, N)

    elif a == 2:  # query
        print(query(1, b, c, 1, N))
