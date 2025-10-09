import sys

input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
M = int(input())


def is_possible(max_thresh):
    temp = 0
    for price in prices:
        temp += min(price, max_thresh)

    if temp > M:
        return False
    return True


l, r = 0, 10**9 + 1
while l < r:
    mid = (l + r) // 2
    if is_possible(mid):
        l = mid + 1
    else:
        r = mid

print(min(max(prices), l - 1))
