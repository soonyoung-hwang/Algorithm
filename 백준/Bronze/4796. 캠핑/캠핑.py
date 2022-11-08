lists = []
while(True):
    L, P, V = list(map(int, input().split()))
    if(P == 0 or L == 0 or V == 0):
        break
        
    lists.append([L, P, V])

for i in range(len(lists)):
    answer = 0
    L, P, V = lists[i]
    answer += L * (V // P)
    answer += min(V%P,L)
    print("Case %d: %d"%(i+1, answer))