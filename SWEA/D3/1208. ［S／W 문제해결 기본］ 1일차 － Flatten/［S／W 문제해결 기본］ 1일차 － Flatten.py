for i in range(10):
    N = int(input())
    
    li = list(map(int, input().split()))
    
    cnt = 0
    while cnt != N:
        li.sort()
        li[-1] -= 1
        li[0] += 1
        cnt += 1
    li.sort()
    print(f"#{i+1} {li[-1]-li[0]}")