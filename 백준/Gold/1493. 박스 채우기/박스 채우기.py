l, w, h = map(int,input().split())
N = int(input())
cubes = []
for _ in range(N):
    cubes.append(list(map(int,input().split())))


volume = l*w*h
answer = 0

def max_put_in(l,w,h,s):
    return (l//s) * (w//s) * (h//s)

for i in range(N):
    cubes[i].append(max_put_in(l,w,h,2**cubes[i][0]))


# print("First volume : ", volume)
# print("First cubes :", cubes)
for i in range(N-1,-1,-1):
    cube = cubes[i]
    put = min(cube[1],cube[2])
    volume -= ((2**cube[0])**3)*put
    answer += put
    
    if(i == 0):
        continue
    
    for j in range(i,0,-1):
        cubes[j-1][2] -= put*((8)**(i-j+1))
    
    if(volume == 0):
        break
    
    

if(volume == 0):
    print (answer)

else:
    print (-1)


