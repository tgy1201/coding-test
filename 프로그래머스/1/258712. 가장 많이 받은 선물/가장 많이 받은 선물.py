from collections import Counter
def solution(friends, gifts):
    answer = {}
    
    take = {}
    give = {}
    
    for i in friends:
        take[i] = []
        give[i] = []
        answer[i] = 0
    
    for v in gifts:
        g, t = map(str, v.split())
        
        take[t].append(g)
        give[g].append(t)
    
    for i in range(len(friends)-1):
        ar = len(give[friends[i]]) - len(take[friends[i]])
        tga = Counter(give[friends[i]])
        
        for j in range(i+1, len(friends)):
            br = len(give[friends[j]]) - len(take[friends[j]])
            tgb = Counter(give[friends[j]])
            
            if((tga[friends[j]] == 0 and tgb[friends[i]] == 0) or tga[friends[j]] == tgb[friends[i]]):
                if(ar > br):
                    answer[friends[i]] += 1
                elif(ar < br):
                    answer[friends[j]] += 1
                else:
                    continue
            elif(tga[friends[j]] > tgb[friends[i]]):
                answer[friends[i]] += 1
            elif(tga[friends[j]] < tgb[friends[i]]):
                answer[friends[j]] += 1
    return max(answer.values())