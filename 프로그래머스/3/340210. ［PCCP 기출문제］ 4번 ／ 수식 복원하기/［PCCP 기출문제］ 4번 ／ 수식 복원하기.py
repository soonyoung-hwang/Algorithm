def solution(expressions):
    answer = []
    
    def val_to_num(num, jisoo):
        return num // (jisoo * jisoo) * 100 + ((num % (jisoo * jisoo)) // jisoo) * 10 + num % jisoo
    
    def num_to_val(jisoo, num):
        return ((num//100) * jisoo * jisoo) + ((num%100)//10) * jisoo + (num%10)
    
    
    def is_possible(jisoo, expression):
        left, right = expression.split("=")
        c = int(right)
        
        if "+" in left:
            a, b = map(int, left.split("+"))
            if num_to_val(jisoo, a) + num_to_val(jisoo, b) == num_to_val(jisoo, c):
                return True
            
        if "-" in left:
            a, b = map(int, left.split("-"))
            if num_to_val(jisoo, a) - num_to_val(jisoo, b) == num_to_val(jisoo, c):
                return True
        return False
        
    def calculate(jisoo, expression):           
        left, right = expression.split("=")
        if "+" in left:
            a, b = map(int, left.split("+"))
            return val_to_num(num_to_val(jisoo, a) + num_to_val(jisoo, b), jisoo)
            
        if "-" in left:
            a, b = map(int, left.split("-"))
            return val_to_num(num_to_val(jisoo, a) - num_to_val(jisoo, b), jisoo)
    
    def find_answer(jisoo, expression):
        return some_int
    
    all_possibles = set([i for i in range(2, 10)])
    for expression in expressions:
        
        temp_max = 0
        for temp_c in expression:
            if ord('1') <= ord(temp_c) <= ord('9'):
                temp_max = max(temp_max, int(temp_c))
            
            for i in range(temp_max+1):
                all_possibles.discard(i)
                    
        if "X" in expression:
            continue
            
        for i in range(2, 10):
            if i not in all_possibles:
                continue
                
            if is_possible(i, expression):
                continue

            all_possibles.discard(i)

    for expression in expressions:
        if "X" in expression:
            tt = set()
            temp_value = 0
            for possible in all_possibles:
                temp_value = calculate(possible, expression)
                tt.add(temp_value)


            if len(tt) == 1:
                tt = expression.replace("X", str(list(tt)[0]))
            else:
                tt = expression.replace("X", "?")
            answer.append(tt)
                
                
    return answer