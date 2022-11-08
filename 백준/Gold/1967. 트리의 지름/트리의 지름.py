import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

from collections import defaultdict

def dfs(n):
    if not routes[n]: # leaf node일 때
        values[n] = [0, 0]
        return
    
    for i in range(len(routes[n])): # 자식노드의 values 먼저 찾는다.
        dfs(routes[n][i][0])
    
    dist_list = []
    maxi = 0
    dist = 0
    
    for i in range(len(routes[n])):
        dist_list.append(values[routes[n][i][0]][1] + routes[n][i][1])  # 자식노드의 가장 긴 뿌리 + 자식노드까지 가는데까지 거리의 합
        maxi = max(maxi, values[routes[n][i][0]][1] + routes[n][i][1]) # 각 자식노드의 가장 긴 뿌리 + 자식노드까지 가는데까지 거리의 최대값
        
    dist_list.sort(reverse=True)
    for i in range(min(2, len(dist_list))):
        dist += dist_list[i]
        
    values[n] = [dist, maxi] # 현재 노드 n 에 대해서 (a가 최고 높은 노드일 때의 트리의 지름, 가장 긴 하나의 뿌리)
    
    return
    

n = int(input())
# n-1개 줄


routes = defaultdict(list)
values = defaultdict(list)
# value[a][0] : a 가 최고 높은 노드일 때, 트리의 지름
# value[a][1] : a 가 최고 높은 노드일 때, 가장 긴 하나의 뿌리

for __ in range(n-1):
    a, b, c = map(int,input().split())
    routes[a].append([b,c])


dfs(1)

answer = 0
for key in values.keys():
    answer = max(answer, values[key][0])

print(answer)