N, M = map(int,input().split())

minimum = [-1]*100001
minimum[N] = 0
count = 0
current = [N]
while(minimum[M] == -1):
#     print(current)
    count += 1
    temp = []
    while(current):
        c = current.pop()
        if(0 <= 2*c <= 100000 and minimum[2*c] == -1):
            temp.append(2*c)
            minimum[2*c] = count
        if(0 <= c-1 <= 100000 and minimum[c-1] == -1):
            temp.append(c-1)
            minimum[c-1] = count
        if(0 <= c+1 <= 100000 and minimum[c+1] == -1):
            temp.append(c+1)
            minimum[c+1] = count
    
    current.extend(temp)

print(minimum[M])