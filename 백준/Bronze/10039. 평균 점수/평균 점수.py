import sys

input = sys.stdin.readline

cnt = 0
for i in range(5):
    n = int(input())

    cnt += max(n, 40)

print(cnt // 5)