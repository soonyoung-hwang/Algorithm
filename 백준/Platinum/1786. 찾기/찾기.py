import sys
input = sys.stdin.readline

def next_start(P):
    # O(m) !
    return_list = [0 for __ in range(m+1)]
    k = 0
    for i in range(1,m+1):
        return_list[i] = k
        if i >= m:
            break
        if P[k] == P[i]:
            k += 1
        else:
            k = return_list[k]
            if P[k] != P[i]:
                k = 0
            else:
                k += 1
            
    return return_list



T = input()[:-1]
P = input()[:-1]
# T = input()
# P = input()

n, m = len(T), len(P)

count = 0
loc = []

nexts = next_start(P)
i = 0
s = 0
while i <= n-m:
    for j in range(s, m):
        if T[i+j] != P[j]:
            break
        if j == m-1:
            j += 1
            
    if j == m:
        count += 1
        loc.append(i+1)
    
    i += max(j-nexts[j],1)
    s = nexts[j]
    
print(count)
if loc:
    print(*loc)
