import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b, c, d, aa, bb, cc, dd = map(int, input().split())

    a = max(a+aa, 1)
    b = max(b+bb, 1)
    c = max(c+cc, 0)
    d = d+dd

    print(1*a + 5*b + 2*c + 2*d)