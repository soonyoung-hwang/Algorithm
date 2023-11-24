from copy import deepcopy

maxi = 0
def solution(info, edges):
    answer = 0
    # 시간복잡도 생각하지마. 갈림길 나오면 무조건 DFS
    routes = [[] for _ in range(len(info))]
    
    for edge in edges:
        a, b = edge
        routes[a].append(b)
    
    # DFS인데, 추가되는 모든 정보를 모두 순회한다.
    
    def dfs(cur_node, explored, left, cnt):
        
        # explored : set of explored node
        global maxi
        maxi = max(cnt, maxi)
        
        new_explored = deepcopy(explored)
        new_explored.add(cur_node)
        
        to_explore = []
        for node in new_explored:
            for next_node in routes[node]:
                if next_node in new_explored:
                    continue
                if info[next_node]:
                    if left > 1:
                        to_explore.append((next_node, new_explored, left-1, cnt))
                else:
                    to_explore.append((next_node, new_explored, left+1, cnt+1))
        
        for nexts in to_explore:
            dfs(nexts[0], nexts[1], nexts[2], nexts[3])
        
        return
    
    dfs(0, set(), 1, 1)
    answer = maxi
    
    
    return answer