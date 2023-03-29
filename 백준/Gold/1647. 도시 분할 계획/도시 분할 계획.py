from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
all_routes = []
roots = defaultdict(int)
for __ in range(M):
    a, b, cost = map(int,input().split())
    all_routes.append([cost, a, b])
    roots[a] = a
    roots[b] = b


def parent(num):
    if roots[num] == num:
        return num
    roots[num] = parent(roots[num])
    return roots[num]

def union_find(a, b):
    if parent(a) < parent(b):
        roots[parent(b)] = a

    elif parent(a) > parent(b):
        roots[parent(a)] = b

all_routes.sort(key = lambda x:-x[0])
cumulative_cost = 0
max_cost = 0

while all_routes:
    cost, a, b = all_routes.pop()
    if parent(a) == parent(b):
        continue
    cumulative_cost += cost
    max_cost = max(max_cost, cost)
    union_find(a, b)
    
    

print(cumulative_cost-max_cost)
