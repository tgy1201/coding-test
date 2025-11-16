import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if n > a or b > a:
    print("Bus")
elif a == b:
    print("Anything")
else:
    print("Subway")