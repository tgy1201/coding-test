import sys, math

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if c % 4 == 0 and (c % 100 != 0 or c % 400 == 0):
        mon[1] = 29

    date = 0
    for i in range(1, b):
        date += mon[i-1]
    date += a

    print(date)
