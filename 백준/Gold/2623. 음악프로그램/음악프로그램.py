N, M = map(int,input().split())
pds = [list(map(int,input().split())) for _ in range(M)]
# before[i] : i의 앞에 처리되야할 숫자, after[i] : i로 인해 처리될 사람들
before = [0 for _ in range(N+1)]
remove = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

members = set()
for pd in pds:
    n, order = pd[0], pd[1:]
    members.add(order[0])
    if len(order) == 1:
        continue
    
    for i in range(n-1):
        remove[order[i]].append(order[i+1])
        before[order[i+1]] += 1
    

answer = []
count = 0
while count < N:
    next_member = -1
    for member in members:
        if before[member] == 0:
            next_member = member
            break
    
    if next_member == -1:
        break
    
    answer.append(next_member)
    visited[next_member] = True
    members.remove(next_member)
    count += 1
    for member in remove[next_member]:
        before[member] -= 1
        members.add(member)

for i in range(1, N+1):
    if not visited[i] and before[i] == 0:
        answer.append(i)


if len(answer) == N:
    for i in range(N):
        print(answer[i])
else:
    print(0)