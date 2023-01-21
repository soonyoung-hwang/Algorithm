# LCS2


"""
     ACAYKP
    C011111
    A112222
    P112223
    C122223
    A123333
    K123344
"""

"""
     PASDOP
    A011111
    K011111
    S012222
    P112223
    D112333
    P112334
"""
# 이런식으로 채우면 잘못된 것 없이 다 채워질거 같은데..?

A = input().rstrip()
B = input().rstrip()
common = [[0 for __ in range(len(B))] for __ in range(len(A))]
found = False
for i in range(len(A)):         # A가 세로
    for j in range(len(B)):     # B가 가로
        if A[i]==B[j]:
            found = True
            common[i][j] = 1
            if i > 0 and j > 0:
                common[i][j] = max(common[i][j], common[i-1][j-1]+1)

        else:
            if j > 0:
                common[i][j] = max(common[i][j], common[i][j-1])
            if i > 0:
                common[i][j] = max(common[i][j], common[i-1][j])

if found:
    answer = []
    i, j = len(A)-1, len(B)-1

    while i >= 0 or j >= 0:
        while j > 0 and common[i][j] == common[i][j-1]:
            j -= 1
        while i > 0 and common[i][j] == common[i-1][j]:
            i -= 1
        
        answer.append(A[i])
        if common[i][j] == 1:
            break
        i -= 1
        j -= 1
        
        # if j > 0:
        #     answer.append(A[i])
            
        #     i -= 1
        #     j -= 1
        # else:
            
        #     answer.append(A[i])
        #     if common[i][j] == 1:
        #         break

    answer_str = ''
    while answer:
        answer_str += answer.pop()
    print(len(answer_str))
    print(answer_str)
else:
    print(0)