import sys
from collections import deque
sys.setrecursionlimit(10**4)

A = input().strip()
B = input().strip()

dq = deque()
boom = len(B)
temp = []

s = 0
e = 0

for i in A:
    dq.append(i)

    if i == B[s]:
        if s == 0:
            temp.append(1)
        else:
            temp[-1] += 1
        s += 1
    elif i == B[0]:
        s = 1
        temp.append(1)
    else:
        s = 0
        temp.clear()

    if temp and temp[-1] == boom:
        temp.pop()
        cnt = 0
        if temp:
            s = temp[-1]
        else:
            s = 0

        while cnt < boom:
            dq.pop()
            cnt += 1

if dq:
    print(''.join(dq))
else:
    print("FRULA")