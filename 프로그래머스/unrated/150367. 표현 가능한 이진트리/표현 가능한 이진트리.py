impossible = False

def solution(numbers):
    answer = []
    global impossible
    
    def check(root, amt):
        global impossible
        if impossible:
            return
        
        if temp_list[root] == 0:
            if temp_list[root-amt] == 1 or temp_list[root+amt] == 1:
                impossible = True
                return
        
        if amt > 1:
            check(root-amt, amt // 2)
            check(root+amt, amt // 2)
        
    
    for number in numbers:
        impossible = False
        m = 0
        
        # 어떤 숫자든지 포화이진트리의 원소의 개수는
        # 2^1-1, 2^2-1, 2^3-1, 2^4-1, ... 이므로
        # 해당 숫자에 맞는 2^m-1 인 m을 구한다.
        # m의 최대는 6 (number가 10^15 일 때)
        
        # 2의 개수가 2^m-1 이면, 
        # 최대 표현 가능한 숫자는 2**(2^m-1)-1
        
        # 1 -> 3 -> 7 -> 15 -> 31 -> 63
        # 1 2 3 4 5 6
    
        for i in range(6, 0,-1):
            if number <= 2**(2**i-1)-1:
                m = i
            
        num = number
        temp_list = []
        
        # number를 2^m-1 길이의 이진수로 바꿔준다.(0포함)
        for i in range(2**m-2, -1,-1):
            temp = num // (2**i)
            temp_list.append(temp)
            num %= (2**i)
        
        
        root = len(temp_list)//2
        amount = (root+1)//2
        
        check(root, amount)
        if impossible:
            answer.append(0)
        else:
            answer.append(1)
            
    
    return answer