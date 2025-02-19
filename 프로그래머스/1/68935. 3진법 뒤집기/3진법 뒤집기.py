def solution(n):
    answer = 0
    q = 0
    data = []
    
    while(n>0):
        if(n > 2):
            q = n % 3
            n = n // 3
            data.append(q)
        
        if(n <= 2):
            data.append(n)
            break
    
    data.reverse()
    for x in range(len(data)):
        answer += data[x]*(3**x)
        
    return answer