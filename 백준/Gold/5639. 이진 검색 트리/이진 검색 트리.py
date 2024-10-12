import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def recover(sub_root, to):
    if sub_root == to:
        return

    mid = sub_root
    for i in range(sub_root, to + 1):
        if arr[i] > arr[sub_root]:
            mid = i - 1
            break
    else:
        mid = to

    # 더 작은 숫자가 있으면
    if sub_root + 1 <= mid:
        route[sub_root][0] = sub_root + 1
        recover(sub_root + 1, mid)

    # 더 큰 숫자가 있으면
    if to >= mid + 1:
        route[sub_root][1] = mid + 1
        recover(mid + 1, to)


def dfs(idx):
    for node in route[idx]:
        if node != -1:
            dfs(node)

    print(arr[idx])


arr = [0]
while True:
    T = input()
    if not T:
        break

    T = int(T.rstrip())
    arr.append(T)

N = len(arr) - 1
route = [[-1, -1] for _ in range(N + 1)]
recover(1, N)  # 복구
dfs(1)