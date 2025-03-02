def solution(n):
    ans = 0
    
    if(n==1):
        return 1
    
    while 1:
        if(n == 1):
            break
        if(n%2 != 0):
            ans +=1
        n = n//2

    return ans+1

2500
1250
625
624
312
156
8