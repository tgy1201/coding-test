def solution(msg):
    dd = {chr(i+65): i+1 for i in range(26)}
    cc = [chr(i+65) for i in range(26)]
    a = ''
    temp = []
    answer = []
    
    for i in msg:
        a += i
        if a in cc:
            temp.append(a)
        else:
            answer.append(cc.index(temp[-1])+1)
            cc.append(a)
            a = i
            temp.append(i)
    answer.append(cc.index(temp[-1])+1)
    return answer