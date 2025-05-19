T = int(input())

for i in range(T):
    N = int(input())
    
    dic = [2,3,5,7,11]
    answer = ""
    
    for j in dic:
        cnt = 0
        while True:
            if N % j != 0:
                break
            cnt += 1
            N //= j
        answer += str(cnt)+" "
        
    print(f"#{i+1} {answer}")
         