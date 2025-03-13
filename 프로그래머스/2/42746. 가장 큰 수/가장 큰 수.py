def solution(numbers):
    a = map(lambda x: [str(x)*(12//len(str(x))),len(str(x))], numbers)
    b = sorted(a, reverse=True)
    answer = ''
    
    for i in b:
        answer += i[0][:i[1]]    
    return str(int(answer))
'''
from collections import deque
def solution(numbers):
    s = deque()
    answer = ''
    
    for i in numbers:
        if len(s) == 0:
            s.append(str(i))
            continue
        cnt = 0
        for j in s:
            if int(str(j)+str(i)) <= int(str(i)+str(j)):
                break
            else:
                cnt +=1
        s.insert(cnt, str(i))
    return ''.join(s)
'''
            
    
            