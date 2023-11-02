import sys

input = sys.stdin.readline


def find_area(A, B, C):
    # 삼각형 넓이 구하기
    a = ((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2) ** (1 / 2)
    b = ((A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2) ** (1 / 2)
    c = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** (1 / 2)
    cosine = (a**2 + b**2 - c**2) / (2 * a * b)
    sine = (1 - cosine**2) ** (1 / 2)

    # 외적 값을 통한, 좌 우 비교
    Ax, Ay = B[0] - A[0], B[1] - A[1]
    Bx, By = C[0] - A[0], C[1] - A[1]
    if Ax * By - Ay * Bx >= 0:
        return 1 / 2 * a * b * sine
    else:
        return -1 / 2 * a * b * sine


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N - 2):
    A = points[0]
    B, C = points[(i + 1)], points[(i + 2)]
    answer += find_area(A, B, C)

answer = abs(answer)
print(f"{answer:.1f}")