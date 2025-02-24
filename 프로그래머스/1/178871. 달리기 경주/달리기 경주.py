def solution(players, callings):
    h = {}
    d = {}
    answer = []
    
    for index, v in enumerate(players):
        h[index] = v
        d[v] = index
    
    for i in callings:
        x = d[i]
        d[i] -= 1
        a = h[d[i]]
        b = d[a]
        
        h[x] = a
        h[b] = i
        d[a] += 1
        
    for i in range(len(players)):
        answer.append(h[i])
    return answer