from heapq import heappush, heappop

answer = 0
def solution(land, height):
    global answer
    
    N = len(land)
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    min_cost = [[10000 for _ in range(N)] for _ in range(N)]
    nextQ = []
    
    def dijkfs(sr, sc, height):
        # dijkstra로 찾는 bfs
        global answer
        
        dd = ((0, 1), (0, -1), (-1, 0), (1, 0))
        heappush(nextQ, (0, sr, sc))
        
        while nextQ:
            cost, r, c = heappop(nextQ)
            if visited[r][c]:
                # 다른 방향에서 이미 체크 했을 경우
                continue
                
            if cost > height:
                answer += cost
            
            visited[r][c] = 1    
            for d in dd:
                nr, nc = r + d[0], c + d[1]
                if nc < 0 or nc > N-1 or nr > N-1 or nr < 0:
                    continue
                if visited[nr][nc]:
                    continue
                dif = abs(land[r][c] - land[nr][nc])
                if min_cost[nr][nc] > dif:
                    min_cost[nr][nc] = dif
                    heappush(nextQ, (dif, nr, nc))
            
    dijkfs(0, 0, height)
    
    
    return answer