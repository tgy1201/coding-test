def solution(n,a,b):
    answer = 0
    a = a - 1
    b = b - 1
    
    for i in range(n // 2):
        if(a//2 == b//2):
            return i+1
        a //= 2
        b //= 2