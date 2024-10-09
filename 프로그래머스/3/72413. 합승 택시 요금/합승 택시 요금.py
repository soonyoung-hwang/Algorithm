MAX = 100000 * 200 + 1

def solution(n, s, a, b, fares):
    answer = MAX
    
    cost = [[MAX for _ in range(n)] for _ in range(n)]
    
    # 전처리
    for i in range(n):
        cost[i][i] = 0
    
    for fare in fares:
        aa, bb, cc = fare
        cost[aa-1][bb-1] = cc
        cost[bb-1][aa-1] = cc
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 중간점이 k일 때, i -> j 의 값 업데이트
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    # 합승 지점이 k 일 때 마다, 최소 값 업데이트
    for i in range(n):
        temp_cost = 0
        temp_cost += cost[s-1][i]
        temp_cost += cost[i][a-1]
        temp_cost += cost[i][b-1]
        answer = min(answer, temp_cost)
        
    return answer