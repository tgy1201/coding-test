import sys, math
from collections import deque

input = sys.stdin.readline

T = int(input())
a = 0

def erasto(x):
    temp = [True] * (x+1)
    temp[0] = False
    temp[1] = False
    answer = []

    for i in range(2, x+1):
        if temp[i]:
            j = 2

            while i*j <= x:
                temp[i*j] = False
                j += 1

    for index, i in enumerate(temp):
        if i:
            answer.append(index)

    return answer


d = erasto(T)

if T == 1:
    print(0)
elif T == 2:
    print(1)
else:
    s = 0
    e = 1
    cnt = d[s] + d[e]

    while s < e:
        if cnt == T:
            a += 1
            e += 1
            cnt += d[e]
        elif cnt > T:
            cnt -= d[s]
            s += 1
        else:
            e += 1
            cnt += d[e]

    if d[-1] == T:
        print(a+1)
    else:
        print(a)