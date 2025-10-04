def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    N = len(A)
    
    b = 0
    for i in range(N):
        if A[i] < B[b]:
            answer += 1
            b += 1
    
    print(answer)
    
    
    return answer