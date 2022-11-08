import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
num = [0]+list(map(int,input().split()))
M = int(input())

dp = [[-1 for __ in range(N+1)] for __ in range(N+1)]
# dynamic program
# -1 : not explored yet
# 0 : False
# 1 : True

def is_palindrome(S:int,E:int):
    if dp[S][E] != -1:
        return dp[S][E]
    
    elif S == E:
        dp[S][E] = 1
        
    elif E-S == 1:
        if num[S] == num[E]:
            dp[S][E] = 1
        else:
            dp[S][E] = 0
    
    elif num[S] != num[E]:
        dp[S][E] = 0
    
    else:
        dp[S][E] = is_palindrome(S+1,E-1)
        
    return dp[S][E]

for __ in range(M):
    S, E = map(int,input().split())
    print(is_palindrome(S,E))

