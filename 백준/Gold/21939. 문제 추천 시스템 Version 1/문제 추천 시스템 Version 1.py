import sys
import heapq
N = int(sys.stdin.readline())
max_heap, min_heap = [], []
check = dict()
current_problem_level = dict()
for _ in range(N): 
    num, level = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, (level, num))
    heapq.heappush(max_heap, (-level, -num))
    current_problem_level[num] = level
    check[(num, level)] = False

result = ""
solved = set()
M = int(sys.stdin.readline())

for _ in range(M):
    query, *nums = sys.stdin.readline().split()
    if query == "add":
        heapq.heappush(min_heap, (int(nums[1]), int(nums[0])))
        heapq.heappush(max_heap, (-int(nums[1]), -int(nums[0])))
        check[(int(nums[0]), int(nums[1]))] = False
        current_problem_level[int(nums[0])] = int(nums[1])
    
    # 가장 어려운 문제 출력
    elif query == "recommend" and int(nums[0]) == 1: 
        tmp = []
        while max_heap:
            level, num = heapq.heappop(max_heap)
            if not check[(-num, -level)] and (-num, -level) not in solved: 
                break
        print(-num)
        heapq.heappush(max_heap, (level, num))
    
    # 가장 쉬운 문제 출력
    elif query == "recommend" and int(nums[0]) == -1:
        tmp = []
        while min_heap:
            level, num = heapq.heappop(min_heap)
            if not check[(num, level)] and (num, level) not in solved: 
                break
        print(num)
        heapq.heappush(min_heap, (level, num))
    
    # 문제 제거
    else:
        problem = int(nums[0])
        level = current_problem_level[problem]
        solved.add((problem, level))