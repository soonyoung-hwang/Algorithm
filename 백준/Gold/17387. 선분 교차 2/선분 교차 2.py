import random

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

answer = 0
def gradient(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def y_axis(x1, y1, x2, y2):
    return y1-x1*gradient(x1, y1, x2, y2)

def is_same(x1, x2):
    if abs(x1-x2) < 0.000001:
        return True
    return False

def overlap(x1, x2, x3, x4):
    # x1 != x2, x3, x4는 상관 X
    if x1 > x2:
        x1, x2 = x2, x1

    if x3 > x4:
        x3, x4 = x4, x3

    # 한 점에서 만난다.
    if is_same(x1, x3) or is_same(x1, x4) or is_same(x2, x3) or is_same(x2, x4):
        return True
    if x1 < x3 < x2 or x1 < x4 < x2:
        return True
    # 포함 되어있다
    if x1 > x3 and x2 < x4:
        return True
    
    return False

# case 1 기울기가 무제한으로 동일
if x1==x2 and x3==x4:
    # print("case 1")
    if is_same(x1, x3) and overlap(y1, y2, y3, y4):
        answer = 1
    else:
        answer = 0
    
# case 3 기울기 다름 (하나는 무제한 일 때)
elif x1==x2 or x3==x4:
    # print("case 3")
    if x1 == x2:
        a2, b2 = gradient(x3, y3, x4, y4), y_axis(x3, y3, x4, y4)
        if overlap(x3, x4, x1, x2):
            y = x1*a2 + b2
            if overlap(y1, y2, y, y) and overlap(y3, y4, y, y):
                answer = 1
    else:
        a1, b1 = gradient(x1, y1, x2, y2), y_axis(x1, y1, x2, y2)
        if overlap(x1, x2, x3, x4):
            y = x3*a1 + b1
            if overlap(y1, y2, y, y) and overlap(y3, y4, y, y):
                answer = 1
        else:
            answer = 0

# case 2 기울기가 무제한이 아니면서 동일
elif (is_same(gradient(x1, y1, x2, y2), gradient(x3, y3, x4, y4))):
    # print("case 2")
    if is_same(y_axis(x1, y1, x2, y2),y_axis(x3, y3, x4, y4)):
        if overlap(x1, x2, x3, x4):
            answer = 1
    else:
        answer = 0

# case 4 기울기가 그냥 다름 -> 공통 점으로 찾는다.
else:
    # print("case 4")
    a1, b1 = gradient(x1, y1, x2, y2), y_axis(x1, y1, x2, y2)
    a2, b2 = gradient(x3, y3, x4, y4), y_axis(x3, y3, x4, y4)
    x = (b2-b1)/(a1-a2)
    if overlap(x1, x2, x, x) and overlap(x3, x4, x, x):
        answer = 1
    else:
        answer = 0

print(answer)
