import sys

n = int(input())
c = []
for _ in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    c[i][0], c[i][1] = c[i][1], c[i][0]

ans = 0

c.sort()
c.reverse()

a = [0,0]

while(c):
    k = c.pop()
    if(k[1] >= a[0]):
        ans += 1
        a[0] = k[0]
    
print(ans)