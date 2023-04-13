from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''    
    count = dict()
    
    min_route = deque()
    if x-r > 0:     # x가 더 아래
        min_route.extend(['u']*(x-r))
        count['u'] = (x-r)
        count['d'] = 0
    elif x-r < 0:   # x가 더 위
        min_route.extend(['d']*(r-x))
        count['d'] = (r-x)
        count['u'] = 0
    else:
        count['d'] = 0
        count['u'] = 0
        
    if y-c > 0:     # y가 더 오른쪽
        min_route.extend(['l']*(y-c))
        count['l'] = (y-c)
        count['r'] = 0
    elif y-c < 0:   # y가 더 왼쪽
        min_route.extend(['r']*(c-y))
        count['r'] = (c-y)
        count['l'] = 0
    else:
        count['r'] = 0
        count['l'] = 0
        
    k -= len(min_route)
    if k < 0 or k%2 != 0:
        return 'impossible'
    
    # 순서 : d, l, r ,u
    cycle = ((n-x)+(y-1))*2
    if cycle != 0:
        times = k // cycle      # cycle + times 만큼 나중에 추가하면 된다.(맨 앞)
        left = k % cycle    

        add_d = min(left // 2, (n-x) - count['d'])
        left -= add_d*2
        min_route.extend(add_d * ['d'])
        min_route.extend(add_d * ['u'])
        if left > 0:
            add_l = min(left // 2, (y-1) - count['l'])
            left -= add_l*2
            min_route.extend(add_l * ['l'])
            min_route.extend(add_l * ['r'])
    
    else:
        times = 0
        left = k
    
    min_route = deque(sorted(list(min_route)))

    if left:                # 그런데도 남아있다? 그러면 -> lr 추가, ud 추가해야한다.
        temp = []
        if y < m:
            for i in range(left//2):
                temp.extend(['r','l'])
        
        elif x > 1:
            for i in range(left//2):
                temp.extend(['u','d'])
        
        if min_route[0] < temp[0]:
            min_route.extend(temp)
        else:
            min_route.extendleft(temp)
    
    if times:
        temp = []
        for i in range(n-x):
            temp.append('d')
        for i in range(y-1):
            temp.append('l')
        for i in range(y-1):
            temp.append('r')
        for i in range(n-x):
            temp.append('u')
        min_route.extendleft(temp)
    
    answer = ''.join(min_route)
    
    return answer