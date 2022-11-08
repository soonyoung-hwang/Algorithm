def divisor(n):
    t = []
    for i in range(2,int(n**(1/2))+1):
        if n%i ==0:
            t.append(i)
    
    for i in range(len(t)):
        t.append(n//t[i])
    
    t.append(n)
    
    t = set(t)
    return t

N = int(input())
arr = []
for __ in range(N):
    arr.append(int(input()))

arr.sort()
temp = []
for i in range(N-1):
    temp.append(arr[i+1]-arr[i])

temp2 = []
for t in temp:
    temp2.append(divisor(t))

k = list(set.intersection(*temp2))
k.sort()

print(*k)