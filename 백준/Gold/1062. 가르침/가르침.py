import itertools
import sys
input = sys.stdin.readline

alphabets = [chr(x) for x in range(ord('a'), ord('z')+1)]
alphabets = set(alphabets)

minimum = []
s = "antatica"
for c in s:
    minimum.append(c)
minimum = set(minimum)
alphabets = list(alphabets.difference(minimum))
alphabets.sort()

N, K = map(int,input().split())
words = [input().rstrip() for __ in range(N)]

if K < 5:
    print(0)
    sys.exit(0)
else:
    K -= 5
    
min_words = []
for word in words:
    temp = []
    for c in word:
        if c in minimum:
            continue
        temp.append(c)
    if len(set(temp)) > K:
        continue
    min_words.append(set(temp))


alphabet_flag = dict()
for a in alphabets:
    alphabet_flag[a] = False

answer = 0
for eachcase in itertools.combinations(alphabets,K):
    for a in eachcase:
        alphabet_flag[a] = True
        
    res = 0
    for word in min_words:
        temp = True
        for s in word:
            if alphabet_flag[s] == False:
                temp = False
                break
        if temp:
            res += 1
    
    for a in eachcase:
        alphabet_flag[a] = False
        
    answer = max(answer,res)
        
print(answer)