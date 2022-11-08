N = int(input())
k = 0

# solution 2
def find(N):
    k = 0
    if(N <= 3):
        m = 0
    
    else:
        s = 3
        m = s
        while(s < N):
            m = s
            k += 1
            s += (s+3+k)

    return k, N-m

def mthn(k,i):
    if(i == 1):
        return "m"
    elif(i <= k+3):
        return "o"
    else:
        kk, ii = find(i-(k+3))
        return mthn(kk,ii)

k, i = find(N)
answer = mthn(k,i)
print(answer)