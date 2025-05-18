from collections import Counter
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    li = []
    for j in range(N):
        row = list(map(int, input().split()))
        li.append(row)
    
    m = -1
    answer = []
    for j in range(N-M+1):
        for k in range(N-M+1):
            sum = 0
            for l in range(M):
                for m in range(M):
                    sum += li[j+l][k+m]
            
            answer.append(sum)
    
    print(f"#{i+1} {max(answer)}")