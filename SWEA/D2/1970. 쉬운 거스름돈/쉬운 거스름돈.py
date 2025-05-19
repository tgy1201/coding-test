T = int(input())

for i in range(T):
    N = int(input())
    
    dic = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = ''
    for j in dic:
        answer += str(N//j)+ " "
        N = N % j
    
    print(f"#{i+1}")
    print(answer)
         