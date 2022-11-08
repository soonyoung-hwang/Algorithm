N = int(input())
a = [int(input()) for __ in range(N)]
a.sort()
for i in range(N):
    print(a[i])