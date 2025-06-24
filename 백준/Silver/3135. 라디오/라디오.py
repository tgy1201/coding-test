import sys

input = sys.stdin.readline

A, B = map(int, input().split())

button = []

N = int(input())

diff = abs(A-B)

for _ in range(N):
    Z = int(input())

    if abs(B-Z) < diff:
        diff = abs(B-Z)

if diff == abs(A-B):
    print(diff)
else:
    print(diff+1)