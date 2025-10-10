def solution(a):
    answer = 0
    
    # i 번째 숫자가 가능한지 체크하려면
    # i 번째 숫자 왼쪽 혹은 오른쪽에 i번째 수 보다 작은게 최대 한 쪽에만 몰려있어야 한다.
    
    left, right = [], []
    current_min = 1_000_000_001
    for i in range(len(a)):
        if current_min < a[i]:
            left.append(1)
            continue
        current_min = a[i]
        left.append(0)
    
    current_min = 1_000_000_001
    for i in range(len(a)-1, -1, -1):
        if current_min < a[i]:
            right.append(1)
            continue
        current_min = a[i]
        right.append(0)
    
    right = right[::-1]
    
    for i in range(len(a)):
        if left[i] + right[i] <= 1:
            answer += 1

    return answer