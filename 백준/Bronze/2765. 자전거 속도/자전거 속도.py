import sys, math

input = sys.stdin.readline

case = 1
pi = 3.1415927

while True:
    a, b, c = map(float, input().split())

    if b == 0:
        break

    inchToMile = a / (12*5280)
    secToHour = c / 3600

    dist = inchToMile * pi * b
    mph = dist / secToHour

    print(f'Trip #{case}: {round(dist, 2):.2f} {round(mph, 2):.2f}')
    case += 1