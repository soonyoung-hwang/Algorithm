import itertools

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

combs = list(map(list, itertools.combinations(range(1,N+1), int(N/2))))
    
def find_total(team):
    s = 0
    for i in range(len(team)):
        for j in range(len(team)):
            s += arr[team[i]-1][team[j]-1]
            
    return s

S = 10000
for i in range(int(len(combs)/2)):
    A = find_total(combs[i])
    B = find_total(combs[-(i+1)])
    C = abs(A-B)
    if(C < S):
        S = C

print(S)