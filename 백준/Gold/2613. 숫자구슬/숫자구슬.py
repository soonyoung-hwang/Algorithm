from collections import deque

N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

answer = []


def is_possible(temp_max):
    global answer

    num_group, num_cnt, tmp = 1, 0, 0
    temp_answer = []
    for num in numbers:
        if num > temp_max:
            return False
        if tmp + num > temp_max:
            temp_answer.append(num_cnt)
            tmp = num
            num_cnt = 1
            num_group += 1
            continue

        tmp += num
        num_cnt += 1

    else:
        if tmp > temp_max:
            return False

        temp_answer.append(num_cnt)

    if M < num_group:
        return False

    answer = temp_answer
    return True


# 이분탐색
l, r = 0, 100 * 300 + 1

while l < r:
    mid = (l + r) // 2
    if is_possible(mid):
        r = mid
    else:
        l = mid + 1

answer = deque(answer)
need = M - len(answer)
real_answer = deque()
# print("initial")
# print(r)
# print(*answer)
# print("need :", need)

while answer and need:
    a = answer.popleft()
    if a == 1:
        real_answer.append(a)
        continue

    times = min(a - 1, need)

    for i in range(times):
        real_answer.append(1)
        a -= 1

    need -= times
    if a > 0:
        real_answer.append(a)


while answer:
    real_answer.append(answer.popleft())

print(r)
print(*real_answer)
