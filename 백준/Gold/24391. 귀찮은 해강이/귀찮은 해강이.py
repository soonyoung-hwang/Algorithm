import sys

input = sys.stdin.readline


# 1. union 함수 정의
def union(x, y):
    # 1-1. 두 건물의 루트 노드 찾기
    x = find(x)
    y = find(y)
    # 1-2. 더 작은 루트 노드에 합치기
    if x > y:
        roots[x] = y
    else:
        roots[y] = x


# 2. find 함수 정의
def find(x):
    # 2-1. 루트 노드를 찾을 때까지 재귀 호출
    if roots[x] != x:
        roots[x] = find(roots[x])
    return roots[x]


n, m = map(int, input().split())
# 3. 루트 노드 리스트 생성
roots = list(range(n + 1))
# 4.
for _ in range(m):
    x, y = map(int, input().split())
    # 노드 연결
    union(x, y)
# 5.
ans = 0
schedule = list(map(int, input().split()))
for i in range(len(schedule) - 1):
    # 두 강의 간 루트 노드가 다를 경우 카운트
    if find(schedule[i]) != find(schedule[i + 1]):
        ans += 1
# 6. 결과 출력
print(ans)