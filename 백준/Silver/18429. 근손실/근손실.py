import sys
input = sys.stdin.readline
n, k = map(int, (input().split()))
arr = list(map(int, input().rstrip().split()))
cnt = 0
result = []
visited = [False] * n
def backtrack(idx, limit):
    if idx == n:
        global cnt
        cnt += 1
        return
    for i in range(n):
        if not visited[i] and (limit + arr[i] - k) >= 500:
            visited[i] = True
            backtrack(idx + 1, limit + arr[i] - k)
            visited[i] = False
    return
backtrack(0, 500)
print(cnt)