import math
T = int(input())

def tree(l):
    if len(l) == 1:
        return l[-1]
    elif len(l) == 2:
        if abs(l[0][1]-l[1][1]) == 2:
            if l[0][1] == 1:
                return l[0]
            else:
                return l[1]
        else:
            if l[0][1] > l[1][1]:
                return l[0]
            elif l[0][1] < l[1][1]:
                return l[1]
            else:
                return l[0]
    
    a = tree(l[:(1+len(l))//2])
    b = tree(l[(1+len(l))//2:])
    
    if abs(a[1]-b[1]) == 2:
        if a[1] == 1:
            return a
        else:
            return b
    else:
        if a[1] > b[1]:
            return a
        elif a[1] < b[1]:
            return b
        else:
            return a

for i in range(T):
    N = int(input())
    
    li = list(map(int, input().split()))
    
    for j in range(len(li)):
        li[j] = [j+1, li[j]]
    
    print(f"#{i+1} {tree(li)[0]}")   