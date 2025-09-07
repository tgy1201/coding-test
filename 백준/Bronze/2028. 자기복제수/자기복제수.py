import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())

    nn = n ** 2

    if n == (nn % (10**len(str(n)))):
        print("YES")
    else:
        print("NO")