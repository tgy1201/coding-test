def calc(l):
    s = ''.join(l)
    
    if len(s)%2 == 0:
        if s[:len(s)//2] == s[len(s):len(s)//2-1:-1]:
            return 1
        else:
            return 0
    else:
        if s[:len(s)//2] == s[len(s):len(s)//2:-1]:
            return 1
        else:
            return 0

for i in range(10):
    N = int(input())
    answer = 0
    
    li = []
    for j in range(8):
        e = input()
        ll = []
        for k in e:
            ll.append(k)
        li.append(ll)
    
    cp = [["0"]*8 for _ in range(8)]
    
    for j in range(8):
        for k in range(8):
            cp[j][k] = li[k][j]
            
    if N == 1:
        print(f"#{i+1} {64}")
    else:
        for j in range(8):
            for k in range(8-N+1):
                answer += calc(li[j][k:N+k])
                answer += calc(cp[j][k:N+k])
    
    print(f"#{i+1} {answer}")