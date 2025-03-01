def solution(s):
    num = '0123456789'
    answer = []
    start = 0
    for i in s:
        if(i==" "):
            start = 0
            answer.append(' ')
        else:
            if(i in num):
                start +=1
                answer.append(i)
                continue
            if(start == 0):
                i = i.upper()
                answer.append(i)
                start +=1
            else:
                i = i.lower()
                answer.append(i)
                start +=1
    return ''.join(answer)