import sys
input = sys.stdin.readline

def find(a):
    if root[a] == -1 or root[a] == a:
        return root[a]

    root[a] = find(root[a])
    return root[a]

def union(a, b):
    if find(a) == find(b):
        return
    elif find(a) < find(b):
        root[find(b)] = find(a)
    else:
        root[find(a)] = find(b)

N, M = map(int, input().split())
root = [i for i in range(N + 1)]  # i의 root는 i
avoid = list(map(int, input().split()))
for i in range(1, len(avoid)):
    root[avoid[i]] = -1

count = 0
parties = [list(map(int, input().split())) for _ in range(M)]
for party in parties:
    grp = party[:]
    n = grp[0]
    if n == 1:
        continue

    for i in range(2, n + 1):
        union(grp[1], grp[i])

for party in parties:
    if find(party[1]) != -1:
        count += 1

print(count)
