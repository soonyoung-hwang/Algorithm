s = input()

k = 0
positive = []
negative = []
flag = False
for i in range(len(s)):
    if(s[i] == "-"):
        if(flag):
            negative.append(int(s[k:i]))
        else:
            positive.append(int(s[k:i]))
        k = i+1
        flag = True
    if(s[i] == "+"):
        if(flag):
            negative.append(int(s[k:i]))
        else:
            positive.append(int(s[k:i]))
        k = i+1
    if(i==len(s)-1):
        if(flag):
            negative.append(int(s[k:i+1]))
        else:
            positive.append(int(s[k:i+1]))

answer = sum(positive)-sum(negative)
print(answer)
