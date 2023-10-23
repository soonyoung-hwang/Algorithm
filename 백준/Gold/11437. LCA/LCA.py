import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MAX_N = 17

N = int(input())
routes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    routes[a].append(b)
    routes[b].append(a)

parents = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
depths = [-1 for _ in range(N + 1)]

# initial setting
stack = []


def DFS(node):
    visited[node] = True

    for i in range(MAX_N + 1):
        temp = 1 << i
        if temp > len(stack):
            break
        parents[node].append(stack[-temp])

    depths[node] = len(stack)
    stack.append(node)

    for _next in routes[node]:
        if visited[_next]:
            continue

        DFS(_next)

    stack.pop()


DFS(1)


def find_LCA(node_a, node_b):
    for i in range(MAX_N, -1, -1):
        if depths[node_a] == depths[node_b]:
            break
        if abs(depths[node_a] - depths[node_b]) >= 1 << i:
            if depths[node_a] > depths[node_b]:
                node_a = parents[node_a][i]
            else:
                node_b = parents[node_b][i]

    if node_a == node_b:
        return node_a

    for i in range(MAX_N, -1, -1):
        if depths[node_a] < (1 << i):
            continue

        if parents[node_b][i] == parents[node_a][i]:
            continue

        node_a = parents[node_a][i]
        node_b = parents[node_b][i]

    node_a = parents[node_a][0]
    node_b = parents[node_b][0]

    return node_a


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(find_LCA(a, b))
