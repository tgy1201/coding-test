import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

if n >= m*2:
    answer = m
else:
    answer = n//2

while k != 0:
    if n > m*2:
        n -= 1
    elif n == m*2:
        n -= 1
        answer -= 1
    else:
        m -= 1

    k -= 1

print(max(0, answer))