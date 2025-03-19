import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    dd = defaultdict(list)
    fee = defaultdict(int)
    
    for i in records:
        time, car, act = map(str, i.split())
        ctime = conv_time(time)
        
        if act == "IN":
            dd[car].append(-ctime)
        else:
            dd[car][-1] += ctime
    
    for i in dd:
        total = 0
        if dd[i][-1] <= 0:
            dd[i][-1] += 1439
        
        ss = sum(dd[i])
        if ss >= fees[0]:
            total += fees[1]
            ss -= fees[0]
            total += math.ceil(ss/fees[2]) * fees[3]
        else:
            total += fees[1]
        
        fee[i] = total
            
    for i in sorted(fee):
        answer.append(fee[i])
    
    return answer
    
def conv_time(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m