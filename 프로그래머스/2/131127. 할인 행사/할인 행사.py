from collections import Counter
import copy
def solution(want, number, discount):
    answer = 0
    dd = {want[x]: number[x] for x in range(len(want))}
    
    for i in range(0, len(discount)):
        d = copy.deepcopy(dd)
        
        for j in discount[i:i+10]:
            if j in d:
                d[j] -= 1
                if d[j] == 0:
                    del d[j]
        if len(d) == 0:
            answer += 1
            
    return answer