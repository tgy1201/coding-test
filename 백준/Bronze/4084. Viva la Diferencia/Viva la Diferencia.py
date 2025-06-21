import sys

input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().split())

    if a == b == c == d == 0:
        break

    cnt = 0
    while True:
        if a == b and b == c and c == d:
            print(cnt)
            break
        i, j, k, l = a, b, c, d
        a = abs(i-j)
        b = abs(j-k)
        c = abs(k-l)
        d = abs(l-i)
        cnt += 1