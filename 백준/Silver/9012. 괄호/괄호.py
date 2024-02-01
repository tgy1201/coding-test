import sys

n = int(sys.stdin.readline())

for x in range(0, n):
    s = input()
    arr = [] * len(s)
    cnt = 0
    for y in range(0, len(s)):
        if s[y] == "(":
            arr.append("(")
            cnt = cnt + 1
        elif s[y] == ")":
            cnt = cnt - 1
            if len(arr) >= 1:
                arr.pop()
    if len(arr) == 0 and cnt == 0:
        print("YES")
    else:
        print("NO")
