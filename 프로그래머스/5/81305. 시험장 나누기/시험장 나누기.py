import sys
sys.setrecursionlimit(10**5)

def solution(k, num, links):
    is_possible = [0]
    threshold = [0]
    div_cnt = [0]
    max_cnt = [k-1]
    
    answer = 0
    
    # "그룹별 최대 트래픽을 최소화" = "인원이 가장 많은 그룹의 인원"을 최소화
    
    # 풀이 : 이분탐색
    # max_people = T
    # T인원 이내로,, k 그룹으로 끊을 수 있나? 체크
    # -> k-1번 만에 그룹 나눌 수 있어?
    # 최대 전체는 10,000개
    
    # dfs
    # dfs인데,, 자식은 둘 중 하나 끊을 수 있음
    # T 넘으면 더 큰거 끊으면 된다.
    
    # leaf로부터,, 
    # 1. 가능하면 위 끊어야 좋고 
    # 2. 다 못 하면 자식 중 더 무거운거 끊으면 된다.
    
    # dfs로 완탐하는데, backtracking 방식으로 몇 번에 끊기는지 체크해줄 거다.
    
    def dfs(idx):
        temp = []
        for nxt in links[idx]:
            if nxt == -1:
                continue
            temp.append(dfs(nxt))
        
        if not temp: # leaf node
            return num[idx]
        
        # not leaf node
        temp.sort(reverse=True)
        
        # (두) 세 개 모두 갖고가기
        if sum(temp) + num[idx] <= threshold[0]:
            return sum(temp) + num[idx]
        
        # 그나마 가벼운거 갖고가기
        elif num[idx] + temp[-1] <= threshold[0]:
            if len(temp) == 2:
                div_cnt[0] += 1
            
            return num[idx] + temp[-1]
        # 둘 다 두고가야할 때
        else:
            div_cnt[0] += len(temp)
            return num[idx]
        
        
    def func_possible(value, root):
        # 1. check each idx is less than threshold
        if max(num) > value:
            return False
        
        # 2. initialize values
        div_cnt[0] = 0
        is_possible[0] = True
        is_possible[0] = False
        threshold[0] = value
        # 3. run dfs
        dfs(root)
        # 4. judge
        if div_cnt[0] <= max_cnt[0]:
            return True
        return False
        
    # 1. find root
    root_set = set([i for i in range(len(num))])
    for link in links:
        root_set.discard(link[0])
        root_set.discard(link[1])
    
    root = list(root_set)[0]
    
    # 2. binary search
    l, r = 0, 100_000_001
    while l < r:
        mid = (l+r) // 2
        if func_possible(mid, root):
            r = mid
        else:
            l = mid + 1
    
    answer = l
    
    return answer