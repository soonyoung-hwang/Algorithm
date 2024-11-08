from collections import deque, defaultdict

dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
def solution(land):
    answer = 0
    
    N, M = len(land), len(land[0])
    
    def coloring(s_r, s_c, color):
        land[s_r][s_c] = color
        count = 1
        Q = deque([])
        Q.append((s_r, s_c))
        
        while Q:
            r, c = Q.popleft()
            for i in range(4):
                nr, nc = r + dd[i][0], c + dd[i][1]
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if land[nr][nc] != 1:
                    continue
                
                land[nr][nc] = color
                Q.append((nr, nc))
                count += 1
                
        color_size[color] = count
        
        
    color_size = defaultdict(int)
    color = 2
    for r in range(N):
        for c in range(M):
            if land[r][c] == 1:
                coloring(r, c, color)
                color += 1
    
    for j in range(M):
        current_gas = 0
        current_set = set()
        for i in range(N):
            if land[i][j] > 0:
                current_set.add(land[i][j])
        
        for num in current_set:
            current_gas += color_size[num]
        
        answer = max(answer, current_gas)

    return answer