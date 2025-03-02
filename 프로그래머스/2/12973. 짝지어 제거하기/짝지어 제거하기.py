def solution(s):
    answer = -1
    l = []
    
    for i in s:
        if(len(l) == 0):
            l.append(i)
        else:
            if(l[-1] == i):
                l.pop()
            else:
                l.append(i)
    
    if(len(l)) != 0:
        return 0
    return 1