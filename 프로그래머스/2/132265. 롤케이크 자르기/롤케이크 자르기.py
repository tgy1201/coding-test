def solution(topping):
    a = set()
    b = set()
    
    aa = []
    bb = []
    answer = 0
    start = 0
    end = len(topping) - 1
    

    for i in range(len(topping)):
        a.add(topping[i])
        b.add(topping[len(topping)-1-i])
        
        aa.append(len(a))
        bb.append(len(b))
    bb.reverse()
    
    for i in range(len(topping)-1):
        if aa[i] == bb[i+1]:
            answer += 1
    return answer
        
'''
def solution(topping):
    answer = 0
    
    for i in range(1, len(topping)):
        if len(set(topping[:i])) == len(set(topping[i:])):
            answer += 1
    return answer
'''