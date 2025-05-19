T = int(input())

for i in range(T):
    N = int(input())
    
    s = set()
    cnt = 0
    temp = 1
    
    while True:
        for j in str(N*temp):
            s.add(j)
        if len(s) == 10:
            break
        temp += 1
    print(f"#{i+1} {temp*N}")
         