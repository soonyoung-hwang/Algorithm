# Dynamic - Union Find Problem
# need to set and find the root
# 우선순위가 없을 땐 무조건 앞에 있는게 우선순위로 잡자. (큰 의미는 없다.)
# 전체 이름의 서로 다른 root 의 갯수를 return 하면 될 듯

from collections import defaultdict
import sys

input = sys.stdin.readline

def union(name1, name2):
    root1, root2 = find(name1), find(name2)
    if root1 == root2:
        return

    # % set root2's root to root1
    tree[root2] = root1
    branches[root1].extend(branches[root2])
    return

def find(name):
    if tree[name] == name:
        return name
    tree[name] = find(tree[name])
    return tree[name]
    
def print_network(name):
    root = find(name)
        
    count = len(branches[root])    
    print(count)
    
T = int(input())
for __ in range(T):
    tree = defaultdict(str)
    branches = defaultdict(list)
    
    n = int(input())
    for __ in range(n):
        name1, name2 = input().split()
        if tree[name1] == '':
            tree[name1] = name1
            branches[name1].append(name1)

        if tree[name2] == '':
            tree[name2] = name2
            branches[name2].append(name2)

        union(name1, name2)
        print_network(name1)
