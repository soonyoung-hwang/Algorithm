# 단어수학
# 각 알파벳의 기대값을 먼저 구한다음에
# 기댓값 대로 sort하면 된다.

import sys
from collections import defaultdict

input = sys.stdin.readline


exepcted_value = defaultdict(int)
answer = 0

N = int(input())
words = []
for __ in range(N):
    words.append(input().rstrip())


for word in words:
    for i in range(len(word)):
        char = word[-(i+1)]
        expected = 10**i
        exepcted_value[char] += expected    

total = []
for key in exepcted_value.keys():
    total.append(exepcted_value[key])


assign = 9
total.sort(reverse=True)


for i in range(len(total)):
    answer += total[i]*assign
    assign -= 1


print(answer)