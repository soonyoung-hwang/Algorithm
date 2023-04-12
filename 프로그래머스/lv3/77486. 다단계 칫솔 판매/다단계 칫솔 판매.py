from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    # 10% 를 계산할 때에는 원 단위에서 절사하며, 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가집니다.
    parent = defaultdict(str)
    temp_answer = defaultdict(int)
    
    
    def result(name, money):
        # update name and money
        # use recursive function to make it easy to implement
        
        to_divide = int(money*0.1)
        if to_divide < 1:
            temp_answer[name] += money
            return
        
        temp_answer[name] += (money - to_divide)
        result(parent[name], to_divide)
        return
    
    for i in range(len(enroll)):
        if referral[i] == '-':
            parent[enroll[i]] = 'center'
        parent[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        result(seller[i], amount[i]*100)
            

    for name in enroll:
        answer.append(temp_answer[name])
    
    return answer