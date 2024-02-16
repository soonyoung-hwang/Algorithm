from collections import deque

def solution(coin, cards):
    answer = 0
    L = len(cards)
    have = [False for _ in range(L+1)]
    yet = [False for _ in range(L+1)]
    for i in range(L//3):
        have[cards[i]] = True
    
    life = 0
    for i in range(1, L//2+1):
        if have[i] and have[(L+1)-i]:
            life += 1
    
    two_coins = deque()
    for i in range(L//3, L):
        if have[(L+1)-cards[i]]:
            continue
        if yet[(L+1)-cards[i]]:
            two_coins.append(i)
        else:
            yet[cards[i]] = True
    
    count = 0
    for i in range(L//3, L, 2):
        if have[(L+1)-cards[i]]:
            if coin > 0:
                coin -= 1
                life += 1
        
        if have[(L+1)-cards[i+1]]:
            if coin > 0:
                coin -= 1
                life += 1
        
        if life > 0:
            life -= 1
        else:
            if coin >= 2 and two_coins[0] <= i+1:
                two_coins.popleft()
                coin -= 2
            else:
                break
                
        count += 1
        
    answer = count + 1
    
    
    return answer