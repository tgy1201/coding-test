import math
T = int(input())

for i in range(T):
    N = int(input())
    
    l = 0
    answer = ""
    for j in range(N):
        s, c = map(str, input().split())
        
        answer += s*int(c)
        l += int(c)
    print(f"#{i+1}")

    for j in range(0, len(answer)//10*10+1, 10):
        print(answer[j:j+10])
        