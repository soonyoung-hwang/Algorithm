# 멀티탭 스케쥴링
# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 
# 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.

# 플러그 빼는 횟수 최소화 하도록 빼는 횟수를 계산해보자.

# 매번 뒤에 남은 것들, 중 우선순위 정해서 우선순위가 가장 낮은거 빼면 된다.
# 가까울 수록 늦게 빼야 한다. (멀 수록 빨리 빼야 한다)

# 1. dictionary[물건] = [순서들]
# 2. heapq 로 콘센트 내 우선순위를 정해두자.

from collections import deque
from collections import defaultdict
import heapq

N, K = map(int,input().split())
items = list(map(int,input().split()))

item_loc = defaultdict(deque)

for i, item in enumerate(items):
    item_loc[item].append(i)

consent = []
answer = 0

for i in range(K):
    item = items[i]
    item_loc[item].popleft()
    
    if consent:
        is_in = False
        for cs in consent:
            if item == cs[-1]:
                is_in = True
                cs[0] = -item_loc[item][0] if item_loc[item] else -100
                heapq.heapify(consent)
                # 다시 heapify 가 안되네..
        if is_in:
            continue
    
    if len(consent) < N:
        prior = item_loc[item][0] if item_loc[item] else 100
        heapq.heappush(consent, [-prior, item])
        continue

    heapq.heappop(consent)
    prior = item_loc[item][0] if item_loc[item] else 100
    heapq.heappush(consent, [-prior, item])
    answer += 1
    
print(answer)
