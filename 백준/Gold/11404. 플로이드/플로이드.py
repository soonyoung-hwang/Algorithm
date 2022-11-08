def update():
    for i in range(1,V+1):
        for j in range(1,V+1):
            for k in range(1,V+1):
                routes[j][k] = min(routes[j][k],routes[j][i]+routes[i][k])
    
    
V = int(input())
E = int(input())
INF = 10000000
routes = [[INF for __ in range(V+1)] for __ in range(V+1)]
answer = [[INF for __ in range(V+1)] for __ in range(V+1)]

for i in range(1,V+1):
    routes[i][i] = 0

for __ in range(E):
    a, b, c = map(int,input().split())
    routes[a][b] = min(routes[a][b],c)
    
# for __ in range(V):
update()
    
for i in range(1,V+1):
    for j in range(1,V+1):
        if routes[i][j] == INF:
            routes[i][j] = 0

for i in range(1,V+1):
    print(*routes[i][1:])