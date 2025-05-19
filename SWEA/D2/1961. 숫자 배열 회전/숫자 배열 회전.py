T = int(input())

def rotate(li):
    li.reverse()
    ll = [["0"]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ll[i][j] = li[j][i]
    ll.reverse()
    return ll

for i in range(T):
    N = int(input())
    
    li = []
    for j in range(N):
        e = list(map(str, input().split()))
        e.reverse()
        li.append(e)
    a = rotate(li)
    b = rotate(a)
    b.reverse()
    c = rotate(b)
    
    a.reverse()
    b.reverse()
    c.reverse()
    
    x = list(map(lambda x: ''.join(x), a))
    y = list(map(lambda x: ''.join(x), b))
    z = list(map(lambda x: ''.join(x), c))
    
    answer = [x,y,z]
    
    ll = [["0"]*len(answer) for _ in range(len(answer[0]))]
    
    for j in range(len(answer[0])):
        for k in range(len(answer)):
            ll[j][k] = answer[k][j]
    
    print(f"#{i+1}")
    for j in ll:
        print(' '.join(j))
            
    