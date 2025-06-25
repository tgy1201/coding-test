import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))

s = 0
e = len(P) - 1
diff = 3e9
answer = []

while s < e:
    temp = P[s] + P[e]

    if temp == 0:
        answer = [P[s], P[e]]
        break

    if abs(temp) < diff:
        diff = abs(temp)
        answer = [P[s], P[e]]

    if temp < 0:
        s += 1
    else:
        e -= 1

print(' '.join(map(str, sorted(answer))))
