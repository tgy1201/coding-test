import sys
input = sys.stdin.readline

n = int(input())
base = int(input())
cnt = 0

for _ in range(n):
    nov = int(input())

    add = 0
    if base > nov:
        add = min(base-nov, 360-(base-nov))
    else:
        add = min(nov-base, 360-(nov-base))
    base = nov
    cnt += add

print(cnt)