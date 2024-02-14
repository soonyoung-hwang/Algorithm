from collections import defaultdict

def solution(edges):
    answer = []
    
    def find_type(point):
        # 도넛 : 자기 자신으로 돌아오고, 더 탐험할 곳 없음
        # 막대 : 더 탐험할 곳 없음
        # 8자 : 처음부터 혹은 계속 가다보면 두 갈래길 나옴
        visited = set()
        visited.add(point)
        
        while True:
            if not routes[point]:
                return 2
            elif len(routes[point]) == 2:
                return 3
            elif routes[point][0] in visited:
                return 1
            else:
                point = routes[point][0]
                visited.add(point)
    
    # 시작점 : 나가는 간선만 있음
    # find starting point
    
    set_fr = set()
    set_to = set()
    routes = defaultdict(list)

    for edge in edges:
        fr, to = edge
        set_fr.add(fr)
        set_to.add(to)
        routes[fr].append(to)
    
    sp = 0
    for fr in set_fr:
        if fr not in set_to:
            if len(routes[fr]) >= 2:
                sp = fr
                break
        
    answer = [sp, 0, 0, 0]
    for nxt in routes[sp]:
        tp = find_type(nxt)
        answer[tp] += 1
        
    return answer