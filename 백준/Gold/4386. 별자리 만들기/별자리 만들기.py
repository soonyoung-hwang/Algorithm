from collections import defaultdict
import heapq


N = int(input())
coordinates = [list(map(float,input().split())) for _ in range(N)]
routes = defaultdict(list)
answer = 0

for i in range(N):
    for j in range(N):
        cd1 = coordinates[i]
        cd2 = coordinates[j]
        if i == j:
            continue
        else:
            distance = ((cd1[0]-cd2[0]) ** 2 + (cd1[1]-cd2[1]) ** 2)**(1/2)
            routes[i].append([distance, j])

done = set()
done.add(0)

edges = []
for dis, nxt in routes[0]:
    heapq.heappush(edges, [dis, nxt])

while edges:
    dis, nxt = heapq.heappop(edges)
    if nxt in done:
        continue

    done.add(nxt)
    answer += dis
    for di, nx in routes[nxt]:
        heapq.heappush(edges, [di, nx])

answer = int(answer*100) / 100
print(answer)