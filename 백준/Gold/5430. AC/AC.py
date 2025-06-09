import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()

    n = int(input())
    if n == 0:
        s = deque(map(str, input().strip().lstrip("[").rstrip("]")))
    else:
        s = deque(map(int, input().strip().lstrip("[").rstrip("]").split(",")))

    rev = 0
    check = 0
    for i in p:
        if i == "R":
            rev += 1
        else:
            if len(s) == 0:
                check = 1
                break
            else:
                if rev % 2 == 0:
                    s.popleft()
                else:
                    s.pop()

    if check == 1:
        print("error")
    else:
        if rev % 2 == 0:
            print(f"[{','.join(map(str, list(s)))}]")
        else:
            print(f"[{','.join(map(str, list(s)[::-1]))}]")