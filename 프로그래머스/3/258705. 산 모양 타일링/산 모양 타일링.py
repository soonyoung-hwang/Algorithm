MOD = 10007

def solution(n, tops):
    answer = 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    # 이때 문제 설명에 따라 만든 모양을 정삼각형 또는 마름모 타일로 빈 곳이 없도록 채우는 
    # 경우의 수를 10007로 나눈 나머지를 return 하도록 solution 함수를 완성해 주세요.
    
    # dp설계
    # 현재 top O -> 다음 top이 있을 때 ( 
    #           -> 다음 top이 없을 때 (
    # 현재 top X -> 다음 top이 있을 때
    #           -> 다음 top이 없을 때
    
    # 가운데를 왼쪽이 먹었을 때 + 오른쪽이 먹었을 때
    
    # 1. 왼쪽이 가운데 세모를 안 먹었을 때
    # 2. 왼쪽이 가운데 세모를 먹었을 때
    
    # 처음이 1이면,
    # dp[0][0] = 3
    # dp[0][1] = 4
    
    # 처음이 0이면,
    # dp[0][0] = 2
    # dp[0][1] = 3
    
    # 다음이 1이면, // 둘 다 안먹었을 때,
    # dp[N][0] = dp[N-1][0] + dp[N-1][1] * 2
    # dp[N][1] = dp[N][0] + dp[N-1][1]
    
    # 다음이 0이면,
    # dp[N][0] = dp[N-1][0] + dp[N-1][1]
    # dp[N][1] = dp[N][0] + dp[N-1][1]
    
    if tops[0] == 1:
        dp[0][0] = 3
        dp[0][1] = 4
    elif tops[0] == 0:
        dp[0][0] = 2
        dp[0][1] = 3
    
    for i in range(1, n):
        if tops[i] == 1:
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]*2) % MOD
            dp[i][1] = (dp[i][0] + dp[i-1][1]) % MOD
        else:
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
            dp[i][1] = (dp[i][0] + dp[i-1][1]) % MOD
    
    answer = dp[n-1][1]
    
    
    return answer