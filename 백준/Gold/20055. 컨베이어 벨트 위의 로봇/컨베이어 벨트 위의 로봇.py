from collections import deque
N, K = map(int,input().split())
upperbelt = deque()
lowerbelt = deque()

all_items = list(map(int,input().split()))
for i in range(N):
    upperbelt.append([all_items[i], False])
    lowerbelt.appendleft([all_items[i+N], False])

zero_num = 0

def show_belts():
    print(*upperbelt)
    print(*lowerbelt)

def move_belt():
    U, L = upperbelt.pop(), lowerbelt.popleft()
    upperbelt.appendleft(L)
    lowerbelt.append(U)
    if upperbelt[N-1][1]:
        upperbelt[N-1][1] = False

def move_robot():
    global zero_num

    for i in range(N-1,-1,-1):
        if upperbelt[i][1] and not upperbelt[i+1][1] and upperbelt[i+1][0]:
            upperbelt[i][1] = False
            upperbelt[i+1][0] -= 1
            if upperbelt[i+1][0] == 0:
                zero_num += 1
            upperbelt[i+1][1] = True
    
    if upperbelt[N-1][1]:
        upperbelt[N-1][1] = False
    
def add_robot():
    global zero_num
    if upperbelt[0][0]:
        upperbelt[0][1] = True
        upperbelt[0][0] -= 1
        if upperbelt[0][0] == 0:
            zero_num += 1

cnt = 1
while True:
    move_belt()
    move_robot()
    add_robot()
    
    if zero_num >= K:
        break
    
    cnt += 1

print(cnt)