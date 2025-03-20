from collections import defaultdict, Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    dd = defaultdict(list)
    
    for i in course:
        for j in orders:
            ll = combinations(sorted(j),i)
            dd[i].extend(list(ll))
    
    for i in dd:
        aa = Counter(dd[i]).most_common()
        mm = - 1
        for i, c in list(aa):
            if c >= mm and c >= 2:
                mm = c
                answer.append(''.join(i))
            else:
                break
    return sorted(answer)