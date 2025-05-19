T = int(input())

def compare(x, y):
    m = -float('inf')
    for i in range(len(x)-len(y)+1):
        sum = 0
        for j in range(len(y)):
            sum += x[i+j]*y[j]
        if m < sum:
            m = sum
    return m

for i in range(T):
    N , M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        print(f"#{i+1} {compare(A, B)}")
    else:
        print(f"#{i+1} {compare(B, A)}")