alphabets = 'abcdefghijklmnopqrstuvwxyz'
a_list = {}

def reset():
    for apb in alphabets:
        a_list[apb] = []

T = int(input())
for _ in range(T):
    reset()
    W = input().rstrip()
    K = int(input())
    for i in range(len(W)):
        a_list[W[i]].append(i)
    
    candidates = []
    for apb in alphabets:
        if len(a_list[apb]) >= K:
            candidates.append(apb)
    
    if not candidates:
        print(-1)
        continue

    a, b = 10000, 0
    for candidate in candidates:
        for i in range(len(a_list[candidate])-K+1):
            length = a_list[candidate][i+K-1] - a_list[candidate][i] + 1
            a = min(a, length)
            b = max(b, length)
    
    print(a, b)
