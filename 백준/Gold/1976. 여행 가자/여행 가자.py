def colorize(i, color):
    # i 도시와 연결되어 있는 모든 도시를 같은 색으로 표시
    stack = [i]
    while stack:
        q = stack.pop()
        if visited[q]:
            continue
        visited[q] = color
        for next_city in routes[q]:
            if not visited[next_city]:
                stack.append(next_city)
            
N = int(input())
M = int(input())
routes = [[] for __ in range(N)] # city num -> 0 ~ N-1
for i in range(N):
    cities = list(map(int,input().split()))
    for j in range(N):
        if cities[j] == 1:
            routes[i].append(j)
            
plan = list(map(int,input().split()))

visited = [0 for __ in range(N)]
color = 1
for i in range(N):
    if visited[i]:
        continue
    colorize(i, color)
    color += 1

flag = True
for i in range(M-1):
    if visited[plan[i]-1] != visited[plan[i+1]-1]:
        flag = False
        break

print("YES" if flag else "NO")