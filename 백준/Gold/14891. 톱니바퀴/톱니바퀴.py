def rotate(wheel, d):
    if d == 1:
        if 1 & wheel:
            wheel += 1 << 8
        wheel >>= 1
        
    elif d == -1:
        wheel <<= 1
        if wheel // (1 << 8) :
            wheel += 1
        wheel %= 1 << 8
    
    return wheel


def opposite(a, b, wheels):
    return (wheels[a] >> 5 ^ wheels[b] >> 1) %2

def find_impact(loc, d , wheels):
    temp = [0,0,0,0]
    temp[loc] = d
    
    if loc == 0:
        if opposite(0,1, wheels):
            temp[1] = -d
            if opposite(1,2, wheels):
                temp[2] = d
                if opposite(2,3,wheels):
                    temp[3] = -d
                    
    elif loc == 1:
        if opposite(0,1,wheels):
            temp[0] = -d
        if opposite(1,2,wheels):
            temp[2] = -d
            if opposite(2,3,wheels):
                temp[3] = d
    
    elif loc == 2:
        if opposite(1,2,wheels):
            temp[1] = -d
            if opposite(0,1,wheels):
                temp[0] = d
        if opposite(2,3,wheels):
            temp[3] = -d
            
    elif loc == 3:
        if opposite(2,3, wheels):
            temp[2] = -d
            if opposite(1,2,wheels):
                temp[1] = d
                if opposite(0,1,wheels):
                    temp[0] = -d
    return temp        


wheels = [int('0b'+input(),2) for __ in range(4)]
n = int(input())
commands = [list(map(int,input().split())) for __ in range(n)]


for command in commands:
    loc, d = command
    temp = find_impact(loc-1, d, wheels)
    for i in range(4):
        wheels[i] = rotate(wheels[i],temp[i])

print((wheels[0] >> 7) + 2 * (wheels[1] >> 7) + 4 * (wheels[2] >> 7)
     + 8 * (wheels[3] >> 7))