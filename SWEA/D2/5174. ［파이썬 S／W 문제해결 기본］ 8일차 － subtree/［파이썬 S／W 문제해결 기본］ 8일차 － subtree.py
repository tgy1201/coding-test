from collections import defaultdict
a = int(input())

def tree(N):
    global cnt
    
    for i in dd[N]:
        cnt += 1
        tree(i)

for i in range(a):
    E, N = map(int, input().split())
    li = list(map(int, input().split()))
    dd = defaultdict(list)
    cnt = 1
    
    for j in range(E):
        dd[li[j*2]].append(li[j*2+1])
    
    tree(N)
    print(f"#{i+1} {cnt}")