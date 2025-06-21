import sys, copy

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    t, n = map(int, input().split())

    s1, s2, s3 = 0, 0, 0

    for i in range(1, n*2+1):
        if i%2==0:
            s3 += i
        else:
            s2 += i
    print(f"{t} {s3//2} {s2} {s3}")