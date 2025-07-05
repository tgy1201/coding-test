import sys, math

input = sys.stdin.readline

SX, SY = map(int, input().split())
EX, EY = map(int, input().split())
PX, PY = map(int, input().split())

if SX != EX and SY != EY:
    print(1)
elif SY == EY:
    if SY == PY:
        if max(SX, EX) > PX > min(SX, EX):
            print(2)
        else:
            print(0)
    else:
        print(0)
elif SX == EX:
    if SX == PX:
        if max(SY, EY) > PY > min(SY, EY):
            print(2)
        else:
            print(0)
    else:
        print(0)