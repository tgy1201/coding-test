def solution(n, w, num):
    answer = 0
    d = {}
    dd = {}
    
    for i in range(w):
        dd[i] = []
        
    for i in range(n):
        q = i // w
        if(q not in d):
            d[q] = [i+1]
        else:
            d[q].append(i+1)
    
    for i in d.keys():
        if(len(d[i]) != w):
            d[i].extend([0]*(w-len(d[i])))
        if(int(i) % 2 == 0):
            continue
        else:
            d[i].reverse()
    
    for i in d.keys():
        for index, j in enumerate(d[i]):
            dd[index].append(j)
            
    for i in dd.keys():
        for index, j in enumerate(dd[i]):
            if(num == j):
                dd[i] = list(filter(lambda x : x != 0, dd[i]))
                answer = len(dd[i]) - index
    return answer