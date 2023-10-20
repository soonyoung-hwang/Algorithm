import sys

input = sys.stdin.readline

def find_cost(a, b):
    visited = [False for _ in range(N + 1)]
    stack = [(a, 0)]

    while stack:
        cur, cur_cost = stack.pop()
        if cur == b:
            return cur_cost

        visited[cur] = True

        for next_node, added_cost in routes[cur]:
            if visited[next_node]:
                continue

            stack.append((next_node, cur_cost + added_cost))


N, M = map(int, input().split())
routes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, cost = map(int, input().split())
    routes[a].append([b, cost])
    routes[b].append([a, cost])

for _ in range(M):
    a, b = map(int, input().split())
    print(find_cost(a, b))
