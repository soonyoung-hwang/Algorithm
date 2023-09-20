N, M = map(int,input().split())
nums = list(map(int,input().split()))


plus = []
minus = []

while nums:
    num = nums.pop()
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort()
minus.sort(reverse=True)

cleared = 0
count = 0

if not minus:
    most_far = plus[-1]
elif not plus:
    most_far = -minus[-1]
else:
    most_far = max(plus[-1], abs(minus[-1]))

while plus:
    carry = M
    count += (plus[-1]*2)
    while carry and plus:
        plus.pop()
        carry -= 1

while minus:
    carry = M
    count += (-minus[-1])*2
    
    while carry and minus:
        minus.pop()
        carry -= 1

answer = count-most_far
print(answer)
