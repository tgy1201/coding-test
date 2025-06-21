import sys, copy

input = sys.stdin.readline

C = int(input())

def prime(x):
    cnt = 0

    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            if x//i == i:
                cnt += 1
            else:
                cnt += 2
    return cnt

for _ in range(C):
    n = int(input())

    print(f"{n} {prime(n)}")