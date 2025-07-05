import sys, math

input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    n = input()

    if int(n) != 100:
        n = n.replace("6","9").replace("0","9")

    answer += int(n)

print(round(answer/N+0.00000001))
