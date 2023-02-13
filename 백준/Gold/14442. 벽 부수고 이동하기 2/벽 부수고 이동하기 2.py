from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())  # N, M, K input
mapp = [list(input().rstrip()) for __ in range(N)]

dd = ((0,1),(0,-1),(1,0),(-1,0))
visited = [[sys.maxsize for __ in range(M)] for __ in range(N)]

answer = -2

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs():
    global answer

    Q = deque([(0, 0, 0)])
    visited[0][0] = 0
    count = 0
    while Q:

        for _ in range(len(Q)):
            r, c, k = Q.popleft()
            if r == N-1 and c == M-1:
                answer = count
                Q = []
                break

            for i in range(4):
                nr, nc = r+dd[i][0], c+dd[i][1]
                if not in_range(nr, nc): continue
                if mapp[nr][nc] == '1':
                    if k < K and visited[nr][nc] > k+1:
                        visited[nr][nc] = k+1
                        Q.append((nr, nc, k+1))
                
                if mapp[nr][nc] == '0':
                    if visited[nr][nc] > k:
                        visited[nr][nc] = k
                        Q.append((nr, nc, k))

        count += 1

bfs()
print(answer+1)