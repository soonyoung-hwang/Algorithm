def solution(tickets):
    answer = []
    hashs = dict()
    l = len(tickets)
    
    for i in range(l):
        if(tickets[i][0] not in hashs.keys()):
            hashs[tickets[i][0]] = [tickets[i][1]]
        else:
            hashs[tickets[i][0]].append(tickets[i][1])
            
    for key in hashs.keys():
        hashs[key].sort()
    
    c = 1
    answer.append("ICN")
    n = "ICN"
    while(c <= l):
        n = hashs[n].pop(0)
        answer.append(n)
        c+=1
        
    return answer