from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    
    # 1번 노드에서 "가장 멀리 떨어진 노드의 개수"
    #       최단 경로로 이동했을 때, 간선의 개수가 가장 많은 노드들
    
    # 딱봐도 deque같은데
    route = defaultdict(list)
    for e in edge:
        route[e[0]].append(e[1])
        route[e[1]].append(e[0])
    
    visited = [False for _ in range(n+1)]
    visited[1] = True
    
    Q = deque()
    for nxt in route[1]:
        Q.append(nxt)
        visited[nxt] = True
    
    while Q:
        temp_answer = []
        for i in range(len(Q)):
            q = Q.popleft()
            for nxt in route[q]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                Q.append(nxt)
            temp_answer.append(q)
    
    answer = len(temp_answer)
    
    return answer