import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def solution(nodes, edges):
    answer = [0, 0]
    # 홀짝트리 / 역홀짝트리
    
    # root면, 연결된 모든 개수가 자식노드
    # root가 아니면, 연결 된 모든 개수 - 1 개가 자식노드
    # 근데 root노드는 무조건 하나
    
    # tree 1 / tree 2 / ... / tree 3
    
    # 1. 노드에 주어진 모든 연결 된 트리를 구한다.
    #   구하면서 ... 각각 연결 된 개수를 적어 놓는다.
    
    # 트리가 끝나면, 연결 된 개수를 토대로 홀짝트리 혹은 역홀짝트리 가능한지 살펴보고 숫자를 업데이트 한다.
    # 원소가 1,000,000 이므로, 배열로 담아도 되긴하는데, 딕셔너리로 담아도 된다.

    routes = defaultdict(list)
    
    for a, b in edges:
        routes[a].append(b)
        routes[b].append(a)
    
    
    def make_tree(node):
        for next_node in routes[node]:
            if visited[next_node]:
                tree[next_node] += 1
                tree[node] += 1
                continue
            
            tree[next_node] += 1
            tree[node] += 1
            visited[next_node] = True
            make_tree(next_node)
        
    visited = defaultdict(bool)
    
    for node in nodes:
        if visited[node]:
            continue
        
        tree = defaultdict(int)
        tree[node] = 0
        visited[node] = True
        make_tree(node)
        
        # 각각 노드마다, 자기가 root일 때, 아닐 때 
        # 지금, 다 자식이니까, 연결 노드 -1 해서, 홀짝인지, 역홀짝인지 맞춰놓고
        # 딱 하나만 그걸 바꿀 수 있는데, 바꾸면 되는지 확인하기
        types = [0, 0]
        for key in tree.keys():
            children = (tree[key] / 2) - 1
            
            if(children % 2 == key % 2):
                types[0] += 1
            else:
                types[1] += 1
        
        if types[0] == 1:
            answer[1] += 1
        if types[1] == 1:
            answer[0] += 1
        
        
    return answer