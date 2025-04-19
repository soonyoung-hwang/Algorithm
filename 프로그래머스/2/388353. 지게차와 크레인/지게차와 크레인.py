from collections import deque

def solution(storage, requests):
    answer = 0
    
    dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    N, M = len(storage), len(storage[0])
    new_storage = [["o" for _ in range(M+2)]]
    for i in range(N):
        new_storage.append(list("o" + storage[i][:] + "o"))
    new_storage.append(["o" for _ in range(M+2)])

    def jigecha(target, is_sync):
        visited = [[False for _ in range(M+2)] for _ in range(N+2)]
        
        visited[0][0] = True
        Q = deque([])
        Q.append((0, 0))
        while Q:
            r, c = Q.popleft()
            
            for d in dd:
                nr, nc = r + d[0], c +d[1]
                if not(0 <= nr < N+2 and 0 <= nc < M+2):
                    continue
                if visited[nr][nc]:
                    continue
                if new_storage[nr][nc] == 'o' or new_storage[nr][nc] == target:
                    visited[nr][nc] = True
                    if new_storage[nr][nc] == 'o':
                        # outside 였으면, 다시 살펴본다.
                        Q.append((nr, nc))
                    else:
                        # target 이었으면 상태 변하고 끝
                        if is_sync:
                            Q.append((nr, nc))
                        new_storage[nr][nc] = 'o'
            
    def crane(target):
        for i in range(N+2):
            for j in range(M+2):
                if new_storage[i][j] == target:
                    new_storage[i][j] = 'o'
    
    for request in requests:
        if len(request) == 1:
            jigecha(request, False)
        
        elif len(request) == 2:
            crane(request[0])
        
        jigecha('o', True)
        
    
    for i in range(N+2):
        for j in range(M+2):
            if new_storage[i][j] != 'o':
                answer += 1
            
    # 외부인지, 아닌지 체크
    # X, x로 변경
    # 외부, 일단 지게차로 빠진 것들
    # x는 crane으로 빠진 것들
    
    
    # count
    # return answer
    
    return answer