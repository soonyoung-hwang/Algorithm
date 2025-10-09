import sys

input = sys.stdin.readline

def find_g(num1, num2):
    set1, set2 = set(), set()
    for i in range(1, int(num1 ** (1 / 2) + 1)):
        if num1 % i == 0:
            set1.add(i)
            set1.add(num1 // i)

    for i in range(1, int(num2 ** (1 / 2) + 1)):
        if num2 % i == 0:
            set2.add(i)
            set2.add(num2 // i)

    T = list(set1.intersection(set2))
    T.sort()
    g = T[-1]
    return g


N = int(input().rstrip())  # N <= 1000
for _ in range(N):
    answer = 0
    b, d = map(int, input().split())  # b, d <= 10**9

    # 1. b와 d의 최대공약수 구하기
    g = find_g(b, d)
    # 2. b_prime찾기 b/g의 배수
    b_prime, d_prime = b // g, d // g
    # 3. 정답은 수식을 벗겨보면.. 아래처럼 된다.
    answer = (b - 1) // d_prime
    print(answer)
