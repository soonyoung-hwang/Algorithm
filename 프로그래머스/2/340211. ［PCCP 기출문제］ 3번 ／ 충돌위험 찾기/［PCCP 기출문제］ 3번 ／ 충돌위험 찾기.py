from collections import defaultdict

def solution(points, routes):
    answer = 0
    
    N = len(routes)     # N : robot의 수
    M = len(routes[0])     # M : 방문해야할 장소의 수
    
    scenarios = [[] for _ in range(20001)]  # 해당 시간에 좌표에 이동한 애들
    
    for i in range(N):  # robot 마다, scenario를 채워준다.
        idx = 0
        r, c = points[routes[i][0]-1]
        scenarios[0].append((r, c))

        for j in range(1, M):
            tr, tc = points[routes[i][j]-1]
            while (r, c) != (tr, tc):
                idx += 1
                if r != tr:
                    r += (tr-r)//abs(tr-r)
                elif c != tc:
                    c += (tc-c)//abs(tc-c)

                scenarios[idx].append((r,c))

    for i in range(20001):
        if not scenarios[i]:
            break

        temp_dict = defaultdict(int)
        for r, c in scenarios[i]:
            temp_dict[(r, c)] += 1
        
        for key in temp_dict.keys():
            if temp_dict[key] > 1:
                answer += 1
    
    return answer