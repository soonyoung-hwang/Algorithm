# 백준 신입사원

# 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
import sys
input = sys.stdin.readline

T = int(input())
for __ in range(T):
    N = int(input())
    scores = []
    score2_to_score1 = dict()
    is_out = [False for __ in range(N+1)]

    for __ in range(N):
        a, b = list(map(int,input().split()))
        scores.append([a,b])
    
    scores2 = sorted(scores, key= lambda x:x[-1])
    scores.sort(key=lambda x:-x[0])
    
    while scores:
        s1, s2 = scores.pop()
        if is_out[s1]:
            continue
        while scores2 and scores2[-1][-1] >= s2:
            t1, t2 = scores2.pop()
            if t2 == s2:
                break
            
            is_out[t1] = True
    
    answer = 0
    for i in range(1, N+1):
        if not is_out[i]:
            answer += 1
    
    print(answer)
