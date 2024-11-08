from collections import deque

def solution(bandage, health, attacks):
    answer = 0
    # 주어진 캐릭터가 끝까지 생존할 수 있는지, 남은 체력을 return
    
    max_hp = health
    current_hp = health
    attacks = deque(attacks)
    cnt = 0
    t, x, y = bandage
    for i in range(1, 1001):
        if attacks and attacks[0][0] == i:
            attack = attacks.popleft()
            current_hp -= attack[1]
            if current_hp <= 0:
                break
            cnt = 0
            if not attacks:
                break
            else:
                continue
        
        current_hp = min(max_hp, current_hp + x)
        cnt += 1
        
        if cnt == t:
            current_hp = min(max_hp, current_hp + y)
            cnt = 0
        
    if current_hp <= 0:
        answer = -1
    answer = -1 if current_hp <= 0 else current_hp
        
    return answer