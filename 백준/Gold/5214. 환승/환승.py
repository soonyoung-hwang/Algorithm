from collections import defaultdict, deque

N, K, M = map(int, input().split())
hypertubes = [list(map(int, input().split())) for _ in range(M)]

connected = defaultdict(list)
tube_visited = [False for _ in range(M)]
city_visited = [False for _ in range(N + 1)]

Q = deque()
answer = -1

for i in range(M):
    for city in hypertubes[i]:
        connected[city].append(i)
        if city == 1:
            tube_visited[i] = True
            Q.append([i, 1])

city_visited[1] = True
while Q:
    tube, count = Q.popleft()  # 현재, 갈 수 있는 tube

    # tube 안에 있는 도시 추가
    for next_city in hypertubes[tube]:
        if city_visited[next_city]:
            continue
        city_visited[next_city] = True

        # 도시에 연결된 튜브 Q에 추가
        for next_tube in connected[next_city]:
            if tube_visited[next_tube]:
                continue
            tube_visited[next_tube] = True
            Q.append([next_tube, count + 1])

    if city_visited[N] == True:
        answer = count + 1
        break

print(answer if N != 1 else 1)