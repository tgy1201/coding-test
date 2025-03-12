def solution(clothes):
    answer = 1
    dd = {}
    
    for i in clothes:
        if i[1] not in dd:
            dd[i[1]] = 1
        else:
            dd[i[1]] += 1
        
    for i in dd.values():
        answer *= i+1
    return answer - 1

'''
from itertools import combinations
def solution(clothes):
    answer = 0
    dd = {}
    
    for i in clothes:
        if i[1] not in dd:
            dd[i[1]] = 1
        else:
            dd[i[1]] += 1
    
    for i in range(1, len(dd)+1):
        for j in list(combinations(dd, i)):
            cnt = 1
            for k in j:
                cnt *= dd[''.join(k)]
            answer += cnt
    return answer
'''