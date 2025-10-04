import sys
from collections import defaultdict

N, X = map(int, input().split())

alphabet = defaultdict(chr)

for i in range(26):
    alphabet[i + 1] = chr(ord("A") + i)

temp_answer = []
if N > X or 26 * N < X:
    answer = "!"
else:
    for i in range(N, 0, -1):
        n = max(1, X - (26 * (i - 1)))
        X -= n
        temp_answer.append(alphabet[n])
    answer = "".join(temp_answer)

print(answer)