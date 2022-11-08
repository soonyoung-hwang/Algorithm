from math import log2

a, b = map(int,input().split())
arr = []
for _ in range(a):
    arr.append(list(map(int,input().split())))

    
arrs = []
arrs.append(arr)

def multi(A,B):
    N = len(A)
    C = []
    for i in range(N):
        t = []
        for j in range(N):
            c = 0
            for k in range(N):
                c += A[i][k]*B[k][j]
            c %= 1000
            t.append(c)
        C.append(t)
        
    return C

repeat = int(log2(b))

while(repeat):
    arrs.append(multi(arrs[-1],arrs[-1]))
    repeat -= 1

b = bin(b)
b = b[2:]

c = [[0 for i in range(a)] for i in range(a)]
for i in range(a):
    c[i][i] = 1

b = list(b)
b.reverse()
b = ''.join(b)

for i in range(len(b)):
    if(b[i] == '1'):
        c = multi(arrs[i],c)

for i in range(a):
    print(*c[i])

