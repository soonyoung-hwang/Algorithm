from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

T = int(input())
Ns, ks = [], []
times = []
orders = []
goals = []

for __ in range(T):
    N, k = map(int,sys.stdin.readline().split())
    time = list(map(int,sys.stdin.readline().split()))
    order = [list(map(int,sys.stdin.readline().split())) for __ in range(k)]
    goal = int(sys.stdin.readline())
    
    Ns.append(N)
    ks.append(k)
    times.append(time)
    orders.append(order)
    goals.append(goal)
    
for i in range(T):
    N, k = Ns[i], ks[i]
    time = times[i]
    order = orders[i]
    goal = goals[i]
    
    before = defaultdict(list)
    
    isroot = [True]*(N+1)
    isroot[0] = False

    for o in order:
        before[o[1]].append(o[0])
        isroot[o[1]] = False

    root = int(isroot.index(True))

    dp = [-1]*(N+1)
    
    def dfs(t):
        if t == root:
            dp[root] = time[t-1]
            return dp[root]
        
        if dp[t] != -1:
            return dp[t]
        
        temp = time[t-1]
        for j in range(len(before[t])):
            temp = max(dfs(before[t][j])+time[t-1],temp)

        dp[t] = temp
        return dp[t]

    dfs(goal)
    print(dp[goal])