import sys, math

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().strip()
    x = math.ceil(len(s) / 3)

    ss = s[:x]
    rs = ss[::-1]

    a = ss+rs+ss
    b = ss+rs[1:]+ss
    c = ss+rs+ss[1:]
    d = ss+rs[1:]+ss[1:]

    if s == a or s == b or s == c or s == d:
        print(1)
    else:
        print(0)