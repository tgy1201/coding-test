def solution(bandage, health, attacks):
    a = {}
    max_health = health
    cnt = 0
    
    for i in attacks:
        a[i[0]] = i[1]
    
    end = max(a.keys())
    
    for i in range(end):
        if(health <= 0):
            return -1
        
        if(i+1 in a.keys()):
            health -= a[i+1]
            cnt = 0
        else:
            health = min(health+bandage[1], max_health)
            cnt += 1
            
            if (cnt == bandage[0]):
                health = min(health+bandage[2], max_health)
                cnt = 0
    if(health <= 0):
        return -1
        
    return health