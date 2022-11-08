from itertools import combinations
import copy

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
    

def count(input_arr):
    # 1. fill the array with 2 (virus) after walling
    arr = copy.deepcopy(input_arr)
    answer = 0
    new_answer = -1
    while(answer != new_answer):
        answer = new_answer
        new_answer = 0
        for i in range(N):
            for j in range(M):
                if(arr[i][j] == 2):
                    if(i-1 >= 0 and arr[i-1][j] != 1):
                        arr[i-1][j] = 2
                    if(i+1 <= N-1 and arr[i+1][j] != 1):
                        arr[i+1][j] = 2
                    if(j-1 >= 0 and arr[i][j-1] != 1):
                        arr[i][j-1] = 2
                    if(j+1 <= M-1 and arr[i][j+1] != 1):
                        arr[i][j+1] = 2
    
    # 2. count the safe area (# of 0) 
        for i in range(N):
            for j in range(M):
                if(arr[i][j] == 0):
                    new_answer += 1
      
    return answer       
        

items = [i for i in range(N*M)]

possibles = list(combinations(items,3))
answer = 0
c = 0
for poss in possibles:
    flag = True
    for one in poss:
        if(arr[one//M][one%M] != 0):
            flag = False

    if(flag):
        for one in poss:
            arr[one//M][one%M] = 1
        c += 1
        k = count(arr)
        answer = max(answer,k)
        for one in poss:
            arr[one//M][one%M] = 0

print(answer)