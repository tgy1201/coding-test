import sys
from collections import deque

input = sys.stdin.readline
s = input().strip()

def cal(a):
    dq = deque()
    ddq = deque()
    temp = ''
    check = 0

    for i in a:
        if check == 0 and i.isalpha():
            dq.append(i)

        if check > 0:
            if i == "(":
                check += 1
            elif i == ")":
                check -= 1

            if check == 0:
                dq.extend(cal(temp))
                temp = ''
            else:
                temp += i
            continue

        if i == "(":
            check = 1
            temp = ''
            continue

        if i == "+" or i == "-":
            while ddq:
                x = ddq.pop()
                dq.append(x)
            ddq.append(i)
        elif i == "*" or i =="/":
            while ddq and (ddq[-1] == "*" or ddq[-1] == "/"):
                x = ddq.pop()
                dq.append(x)
            ddq.append(i)

    while ddq:
        x = ddq.pop()
        dq.append(x)

    return dq

print(''.join(cal(s)))
