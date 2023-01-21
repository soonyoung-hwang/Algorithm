#  중량제한
# 다리의 최대 중량을 견디며 옮길 수 있는 가장 큰 중량의 양
# 이분탐색 + dfs 경로 탐색
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
routes = [[] for __ in range(10001)]   # routes[i] = i에서 갈 수 있는 [섬, 중량] 의 list

for _ in range(M):
    A, B, weight = map(int,input().split())
    routes[A].append([B, weight])
    routes[B].append([A, weight])

start, end = map(int,input().split())
# print("routes", routes)

# 중복 처리 : 두 섬을 잇는 가장 높은 무게만 필요하다.
# visited를 먼저 하고 넣으면 처리해줄 필요 없다.
for route in routes:
    route.sort(reverse=True)

def is_possible(weight):
    visited = [False for __ in range(10001)]
    stack = [start]
    visited[start] = True
    
    while stack:
        q = stack.pop()
        if q == end:
            return True

        for _next in routes[q]:
            n, w = _next
            if w < weight:
                continue
            if visited[n]:
                continue
            visited[n] = True
            stack.append(n)
            
    return False

l, r = 1, 1_000_000_001
while l < r:
    mid = (l+r)//2
    if is_possible(mid):
        l = mid+1
    else:
        r = mid

answer = l-1
print(answer)