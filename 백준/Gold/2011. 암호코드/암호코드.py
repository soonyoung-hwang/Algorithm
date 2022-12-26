num = input()
dp = [1 for _ in range(len(num)+1)]
fixed = [False for _ in range(len(num)+1)]

def check(i):
    if int(num[-i]+num[-i+1]) <= 26:
        return True
    return False

is_wrong = False
next_fixed = False
if num[-1] == '0':
    next_fixed = True
if num[0] == '0':
    is_wrong = True

for i in range(2,len(num)+1):
    if next_fixed and (int(num[-i]) == 0 or int(num[-i]) > 2):
        # when previous was 0 and current is 0 or 3,4,5,6,7,8,9 -> wrong
        is_wrong = True
        break
    elif num[-i] == '0':
        # when previous was not 0, but current is 0
        fixed[i-1] = True
        next_fixed = True # tell next_num that i'm 0
        dp[i] = dp[i-1]
    
    elif next_fixed:
        # when previous was 0, and currnet is 1 or 2 -> this num also should be fixed
        next_fixed = False
        fixed[i-1] = True
        dp[i] = dp[i-1]
    else:
        # when previous was not 0, current is not 0
        if not fixed[i-2] and check(i) : # if previous is not fixed and check
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
        

print(dp[len(num)]%1000000 if not is_wrong else 0)