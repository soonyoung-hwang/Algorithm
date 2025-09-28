from collections import defaultdict

def solution(coin, cards):
    answer = 0
    
    N = len(cards)
    my_card = defaultdict(bool)
    pass_card = defaultdict(bool)
    
    life = 0

    for i in range(N//3):
        card = cards[i]
        my_card[card] = True
        if my_card[N+1-card]:
            life += 1
    
    two_coins = 0
    cur_round = 1
    for i in range(N//3, N, 2):
        # 뽑은 card 처리
        for card in (cards[i], cards[i+1]):
            pass_card[card] = True
            if coin == 0:
                continue
                
            if my_card[N+1-card]:
                my_card[card] = True
                coin -= 1
                life += 1
                
            if pass_card[N+1-card]:
                two_coins += 1
        
        # 목숨 처리
        if life > 0:
            life -= 1
            cur_round += 1
            continue
        
        if coin > 1 and two_coins:
            two_coins -= 1
            coin -= 2
            cur_round += 1
            continue

        break
        
    answer = cur_round
    return answer