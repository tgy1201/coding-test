import sys
input = sys.stdin.readline

while True:
    sen = input().strip()

    if sen == "END":
        break

    print(sen[::-1])