from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline

cube = []
orders = ['w', 'y', 'r', 'o', 'g', 'b']
for order in orders:
    cube.append([[order for __ in range(3)] for __ in range(3)])

# (면, 위치) : 위치 0 = 위 행 ; 1 = 아래 행 ; 2 = 왼쪽 열 ; 3 = 오른쪽 열
effect = []
effect.append([(3, 0), (5, 0), (2, 0), (4, 0)])    # U 기준 (시계방향)
effect.append([(3, 1), (4, 1), (2, 1), (5, 1)])    # D 기준

effect.append([(0, 1), (5, 2), (1, 1), (4, 3)])    # F 기준
effect.append([(0, 0), (4, 2), (1, 0), (5, 3)])    # B 기준

effect.append([(0, 2), (2, 2), (1, 3), (3, 3)])    # L 기준
effect.append([(0, 3), (3, 2), (1, 2), (2, 3)])    # R 기준

loc = defaultdict()
loc[(0, 0)] = [(0, 2), (0, 1), (0, 0)]
loc[(0, 1)] = [(2, 0), (2, 1), (2, 2)]
loc[(0, 2)] = [(0, 0), (1, 0), (2, 0)]
loc[(0, 3)] = [(2, 2), (1, 2), (0, 2)]

loc[(1, 0)] = [(0, 2), (0, 1), (0, 0)]
loc[(1, 1)] = [(2, 0), (2, 1), (2, 2)]
loc[(1, 2)] = [(0, 0), (1, 0), (2, 0)]
loc[(1, 3)] = [(2, 2), (1, 2), (0, 2)]

loc[(2, 0)] = [(0, 2), (0, 1), (0, 0)]
loc[(2, 1)] = [(2, 0), (2, 1), (2, 2)]
loc[(2, 2)] = [(0, 0), (1, 0), (2, 0)]
loc[(2, 3)] = [(2, 2), (1, 2), (0, 2)]

loc[(3, 0)] = [(0, 2), (0, 1), (0, 0)]
loc[(3, 1)] = [(2, 0), (2, 1), (2, 2)]
loc[(3, 2)] = [(0, 0), (1, 0), (2, 0)]
loc[(3, 3)] = [(2, 2), (1, 2), (0, 2)]

loc[(4, 0)] = [(0, 2), (0, 1), (0, 0)]
loc[(4, 1)] = [(2, 0), (2, 1), (2, 2)]
loc[(4, 2)] = [(0, 0), (1, 0), (2, 0)]
loc[(4, 3)] = [(2, 2), (1, 2), (0, 2)]

loc[(5, 0)] = [(0, 2), (0, 1), (0, 0)]
loc[(5, 1)] = [(2, 0), (2, 1), (2, 2)]
loc[(5, 2)] = [(0, 0), (1, 0), (2, 0)]
loc[(5, 3)] = [(2, 2), (1, 2), (0, 2)]


def rotate(target, is_counter):
    # part 1 : rotate target 면
    side = cube[target]
    for i in range(2):
        if not is_counter:
            side[0][0], side[0][1], side[0][2], side[1][2], \
            side[2][2], side[2][1], side[2][0], side[1][0] = \
                side[1][0], side[0][0], side[0][1], side[0][2], \
                side[1][2], side[2][2], side[2][1], side[2][0]

        else:
            side[0][0], side[0][1], side[0][2], side[1][2], \
            side[2][2], side[2][1], side[2][0], side[1][0] = \
                side[0][1], side[0][2], side[1][2], side[2][2], \
                side[2][1], side[2][0], side[1][0], side[0][0]

    # part 2 : rotate effected 면
    # 돌릴 색 모두 Q에 저장
    Q = deque()

    for which, loca in effect[target]:
        for r, c in loc[(which ,loca)]:
            Q.append(cube[which][r][c])

    # 3번 씩 shift = 사이드 색 돌리기
    if not is_counter:
        for i in range(3):
            Q.appendleft(Q.pop())
    else:
        for i in range(3):
            Q.append(Q.popleft())

    # 돌린 색 그대로 다시 큐브에 새기기
    temp_loc = 0
    for which, loca in effect[target]:
        for r, c in loc[(which ,loca)]:
            cube[which][r][c] = Q[temp_loc]
            temp_loc += 1




T = int(input())
for __ in range(T):
    cube = []
    orders = ['w', 'y', 'r', 'o', 'g', 'b']
    for order in orders:
        cube.append([[order for __ in range(3)] for __ in range(3)])

    N = int(input())
    cmds = input().rstrip().split()
    for cmd in cmds:
        c, d = cmd[0], cmd[1]

        if c == 'U':
            target = 0
        elif c == 'D':
            target = 1
        elif c == 'F':
            target = 2
        elif c == 'B':
            target = 3
        elif c == 'L':
            target = 4
        elif c == 'R':
            target = 5

        if d == '+':
            counter_clockwise = False
        elif d == '-':
            counter_clockwise = True

        rotate(target, counter_clockwise)

    for i in range(3):
        print(''.join(cube[0][i]))