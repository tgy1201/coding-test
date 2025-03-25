def solution(a, b):
    answer = 0
    
    cnt = 0
    if(a>b):
        cnt = a
        a = b
        b = cnt
    
    for i in range(b, a-1, -1):
        answer += i
    return answer