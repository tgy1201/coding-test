import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    answer = 0
    for _ in range(k):
        answer += 0.5
        answer *= 2

    print(int(answer))