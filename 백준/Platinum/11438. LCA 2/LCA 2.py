"""
이틀 고민하고 못 풀었다.
풀이참조: https://www.crocus.co.kr/660

# LCA2
1. dfs를 통해서 자신의 부모를 구한다.
2. 이중 for문을 통해 조상을 세팅한다.
    parents[j][i-1] = j의 2^i-1 만큼 위에 있는 조상
3. 두 노드의 가장 가까운 조상(부모) 출력
    1) 두 노드 높이를 맞춤
    2) 같은 높이일 경우, 두 노드의 값이 같으면 종료
    3) 같은 높이일 경우, 두 노드의 값이 다르면 두 노드의 높이를 올려가며 확인
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


#  dfs를 통해 완전 탐색을 하면서, 
#       노드의 depth를 정의하고
#       stack을 이용해 모든 노드의 부모를 구한다.
stack = []
def dfs(val, d):
    stack.append(val)
    depth[val] = d

    for _next in connected[val]:        
        if depth[_next]:    # 이미 방문했다면 스킵
            continue
        
        # 부모 setup
        i = 1
        c = 0
        while i <= len(stack):
            parents[_next][c] = stack[-(1+i-1)]
            i *= 2
            c += 1

        dfs(_next, d+1)
    
    stack.pop()

def LCA(num1, num2):
    # 같은 높이 맞추기
    if depth[num1] < depth[num2]:
        num1, num2 = num2, num1

    for i in range(MAX_DEGREE-1, -1, -1):
        if depth[num1] == depth[num2]:
            break
        if (depth[num1] - depth[num2]) >= 1<<i:
            num1 = parents[num1][i]

    if num1 == num2:
        return num1

    # 공통조상 찾기 (CA : Common Ancestor)
    for i in range(MAX_DEGREE-1, -1, -1):
        if parents[num1][0] == parents[num2][0]:
            break
        if parents[num1][i] != parents[num2][i]:
            num1 = parents[num1][i]
            num2 = parents[num2][i]

    # while parents[num1][0] != parents[num2][0]:
    #     i = MAX_DEGREE-1
    #     while i > 0:
    #         if parents[num1][i] != parents[num2][i]:
    #             break
    #         CA = i
    #         i -= 1

    #     num1 = parents[num1][CA-1]
    #     num2 = parents[num2][CA-1]

    return parents[num1][0]
    

MAX_DEGREE = 17
N = int(input())
connected = [[] for __ in range(N+1)]
depth = [0 for __ in range(N+1)]

for __ in range(N-1):
    a, b = map(int,input().split())
    connected[a].append(b)
    connected[b].append(a)

depth[1] = 1
parents = [[0 for __ in range(MAX_DEGREE)] for __ in range(N+1)]
dfs(1,1)

M = int(input())
for __ in range(M):
    a, b = map(int,input().split())
    print(LCA(a,b))
