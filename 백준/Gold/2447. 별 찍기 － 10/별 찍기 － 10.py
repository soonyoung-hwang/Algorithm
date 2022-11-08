from math import log

N = int(input())

arr = [[" " for _ in range(N)] for _ in range(N)]

arr[0][0] = "*"


k = int(log(N))
n = 1



def copy(n, i, j):
    # copy previous array at the sqaure starts with (i,j)
    # the size of copying is n x n
    global arr
    
    # index error when n is 6
    for ii in range(0,int(3**(n-1))):
        for jj in range(0,int(3**(n-1))):
            arr[int(i+ii)][int(j+jj)] = arr[int(ii%int(3**(n-1)))][int(jj%int(3**(n-1)))]
            
    return

while(n <= k):
    for i in range(0,int(3**n),int(3**(n-1))):
        for j in range(0,int(3**n),int(3**(n-1))):
            if(i==0 and j==0):
                continue
            if(i==int(3**(n-1)) and j == int(3**(n-1))):
                continue
            
            copy(n, i, j)
            
    n += 1

for i in range(N):
    print(''.join(arr[i]))


