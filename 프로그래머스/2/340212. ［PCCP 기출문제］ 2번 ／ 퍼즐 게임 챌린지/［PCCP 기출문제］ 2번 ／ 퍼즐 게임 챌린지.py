import sys

def solution(diffs, times, limit):
    answer = 0
    
    # 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하려고 합니다. 
    # 난이도, 소요 시간은 모두 양의 정수며, 숙련도도 양의 정수여야 합니다.
    
    # diffs times limit

    N = len(times)
    
    def check(level):
        total = 0
        
        time_prev = 0
        for i in range(N):
            if diffs[i] <= level:
                total += times[i]
            else:
                total += (times[i] + time_prev) * (diffs[i] - level)
                total += times[i]
            time_prev = times[i]
            
            if total > limit:
                return False
        return True
            
    
    l, r = 1, sys.maxsize
    while l < r:
        mid = (l+r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    
    return r