from collections import Counter
def solution(str1, str2):
    answer = 0
    s = 'abcdefghijklmnopqrstuvwxyz'
    str1 = str1.lower()
    str2 = str2.lower()
    
    a = []
    b = []

    for i in range(0, len(str1)-1):
        if(str1[i] not in s or str1[i+1] not in s):
            continue
        a.append(f"{str1[i]}{str1[i+1]}")
        
    for i in range(0, len(str2)-1):
        if(str2[i] not in s or str2[i+1] not in s):
            continue
        b.append(f"{str2[i]}{str2[i+1]}")
         
    d = Counter(a)
    e = Counter(b)
    
    if(len(a) == 0 and len(b) == 0):
        return 65536
    cnt = 0
    cnt2 = 0
    for i in d.keys():
        if(i in e.keys()):
            cnt += min(d[i], e[i])
            cnt2 += max(d[i], e[i])
        else:
            cnt2 += d[i]
    
    for i in e.keys():
        if(i not in d.keys()):
            cnt2 +=e[i]

    return int(cnt/cnt2*65536)