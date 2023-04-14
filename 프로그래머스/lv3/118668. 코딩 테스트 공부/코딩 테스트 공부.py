from heapq import heappush, heappop

def solution(alp, cop, problems):
    answer = 0
    # second solution is to use dijkstra to solve this problem
    # 해당 자리에서 갈 수 있는 최단거리 이동
    # 그 자리들 q에 담는다.
    # 그 자리에서 갈 수 있는 모든 거리 이동
    # 선택지를 다 넣는거야.
    hq = [(0, alp, cop)]
    alp_need, cop_need = 0, 0
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost_add = problem
        alp_need = max(alp_need, alp_req)
        cop_need = max(cop_need, cop_req)
    


    visited = [[False for _ in range(151)] for _ in range(151)]
    while hq:    
        cost, al, co = heappop(hq)
        if visited[al][co]:
            continue
        visited[al][co] = True
        
        if al >= alp_need and co >= cop_need:
            answer = cost
            break
        
        if not visited[min(150, al+1)][min(150,co)]:
            heappush(hq, (cost + 1, min(150,al+1), min(150,co)))
        if not visited[min(150,al)][min(150,co+1)]:
            heappush(hq, (cost + 1, min(150,al), min(150,co+1)))
            
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost_add = problem
            if al >= alp_req and co >= cop_req:
                if not visited[min(150, al+alp_rwd)][min(150,co+cop_rwd)]:
                    heappush(hq, (cost+cost_add, min(150, al+alp_rwd), min(150,co+cop_rwd)))
                
        
            
    return answer