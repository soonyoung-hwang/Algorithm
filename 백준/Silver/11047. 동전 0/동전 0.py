line, total = input().split()
coins = []
total = int(total)
answer = 0
for i in range(int(line)):
    coins.append(int(input()))


while(total):
    coin = coins.pop()
    answer += total//coin
    total = total - ((total//coin) * coin)

    
print(answer)