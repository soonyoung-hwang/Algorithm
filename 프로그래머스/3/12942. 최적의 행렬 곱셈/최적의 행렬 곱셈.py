import sys

def solution(matrix_sizes):
    answer = 0
    # 모든 행렬을 곱하기 위한 최소 곱셈 연산의 수를 return 하도록
    # (a b) (c d)
    # (a b c) (d)
    # 1 - 10
    # (1 - 2) x (1 - 8)
    # ....
    
    N = len(matrix_sizes)
    dp = [[sys.maxsize for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
        
    # dp[i][j] : i 부터 j 까지의 최소값
    # dp[i][j] = min(dp[i][i+1] * dp[i+1][j], ....dp[i][j-1] * dp[j-1][j])
    
    
    def find(l, r):
        if dp[l][r] != sys.maxsize:
            return dp[l][r]
        
        if r - l == 1:
            dp[l][r] = matrix_sizes[l][0] * matrix_sizes[l][1] * matrix_sizes[r][1]
            return dp[l][r]
        
        for i in range(l, r):
            dp[l][r] = min(dp[l][r], find(l, i) + find(i+1, r) \
                           + matrix_sizes[l][0] * matrix_sizes[i][1] * matrix_sizes[r][1])
        
        return dp[l][r]

    answer = find(0, N-1)
    
    return answer