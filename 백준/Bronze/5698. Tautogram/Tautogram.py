import sys

input = sys.stdin.readline

while True:
    s = list(map(str, input().strip().split()))

    if s[0] == "*":
        break

    check = "Y"

    f = s[0][0].upper()
    for i in s:
        if i[0].upper() != f:
            check = "N"
            break

    print(check)