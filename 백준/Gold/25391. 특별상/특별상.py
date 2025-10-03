import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, K = map(int, input().split())
a_score = []
b_score = []

for i in range(N):
    a, b = map(int, input().split())
    a_score.append((a, i))
    b_score.append((b, i))

b_loc = defaultdict(int)
a_loc = defaultdict(int)

# 10**5
a_score.sort(reverse=True)
b_score.sort(reverse=True)

for i in range(N):
    _, loc = b_score[i]
    b_loc[loc] = i
    _, loc = a_score[i]
    a_loc[loc] = i

answer = 0
left = M
chosen = set()
for i in range(N):
    score, loc = a_score[i]
    if b_loc[loc] < K:  # K번 순위에 들어갈 때-> 아무것도 안 한다.
        continue
    # K번 순위에 안 들어갈 때
    # 특별 선수로 뽑아야 됨
    if left > 0:
        left -= 1
        answer += score
        chosen.add(loc)

    if left == 0:
        break

cnt = 0
for i in range(N):
    _, loc = b_score[i]
    if loc in chosen:
        continue

    answer += a_score[a_loc[loc]][0]
    cnt += 1
    if cnt == K:
        break

print(answer)
