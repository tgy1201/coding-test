T = int(input())

for i in range(T):
    li = list(map(int, input().split()))
              
    a = 60*li[0] + li[1]
    b = 60*li[2] + li[3]
    c = 0
    
    if ((a+b)//60)%12 == 0:
        c = 12
    else: 
        c = ((a+b)//60)%12
        
    print(f"#{i+1} {c} {(a+b)%60}")