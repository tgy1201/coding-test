def solution(n, k):
    answer = 0
    
    s = ""
    dd = []
    for i in convert(n,k):
        if i != 0:
            s += str(i)
        else:
            if s != "":
                dd.append(s)
            s = ""
    if s != "":
        dd.append(s)
        
    for i in dd:
        if prime(int(i)):
            answer += 1
            
    return answer

def convert(n, k):
    s = []
    while n != 0:
        a = n % k
        n //= k
        s.append(a)
    s.reverse()
    return s

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        