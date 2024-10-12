from collections import deque

stack_a = []
stack_b = []
answer = 1001


def possible(A):
    a = A[0]
    n = len(A)

    visited = [0 for _ in range(N + 1)]
    visited[a] = 1

    Q = deque([a])
    ttt = 0
    while Q:
        cur_node = Q.popleft()
        for next_node in routes[cur_node]:
            if next_node not in A:
                continue
            if visited[next_node] == 1:
                continue
            visited[next_node] = 1
            Q.append(next_node)

    if sum(visited) == n:
        return True

    return False


def calculate():
    if not stack_a or not stack_b:
        return 1001

    if possible(stack_a) and possible(stack_b):
        a_total, b_total = 0, 0
        for i in range(len(stack_a)):
            a_total += populates[stack_a[i] - 1]
        for i in range(len(stack_b)):
            b_total += populates[stack_b[i] - 1]

        return abs(a_total - b_total)
    else:
        return 1001


def dfs(idx):
    global answer

    if idx == N + 1:
        answer = min(answer, calculate())
        return

    stack_a.append(idx)
    dfs(idx + 1)
    stack_a.pop()

    stack_b.append(idx)
    dfs(idx + 1)
    stack_b.pop()


N = int(input())
populates = list(map(int, input().split()))
routes = [[]] + [[] for _ in range(N)]
for cur in range(1, N + 1):
    info = list(map(int, input().split()))
    routes[cur].extend(info[1:])

dfs(1)
print(answer if answer != 1001 else -1)
