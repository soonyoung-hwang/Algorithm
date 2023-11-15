from collections import deque
import sys
input = sys.stdin.readline

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

N, M, K = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(N)]
target = input().rstrip()

dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(len(target))]

for i in range(N):
    for j in range(M):
        if arr[i][j] == target[0]:
            dp[0][i][j] += 1

for i in range(1, len(target)):
    to_explore = []
    for r in range(N):
        for c in range(M):
            if dp[i-1][r][c]:
                to_explore.append((r, c))
    
    while to_explore:
        r, c = to_explore.pop()
        for move in moves:
            for k in range(1, K+1):
                nr, nc = r + move[0]*k, c + move[1]*k
                if not (0 <= nr < N and 0 <= nc < M):
                    break
                if arr[nr][nc] == target[i]:
                    dp[i][nr][nc] += dp[i-1][r][c]
                    continue

answer = 0
for r in range(N):
    for c in range(M):
        answer += dp[len(target)-1][r][c]

print(answer)