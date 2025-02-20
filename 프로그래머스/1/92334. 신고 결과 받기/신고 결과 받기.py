from collections import Counter
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    r = list(set(report))
    
    a = dict()
    
    for i in r:
        if(i.split()[1] not in a.keys()):
            a[i.split()[1]] = [i.split()[0]]
        else:
            a[i.split()[1]].append(i.split()[0])
            
    b = sum(list(filter(lambda x: len(x) >= k,a.values())), [])
    c = dict(Counter(b))
    
    for i in c.keys():
        answer[id_list.index(i)] = c[i] 
    return answer