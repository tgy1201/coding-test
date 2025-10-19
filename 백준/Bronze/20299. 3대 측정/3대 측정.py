import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
answer = []
cnt = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    total = a + b + c

    if k > total:
        continue

    if a < l or b < l or c < l:
        continue

    cnt += 1
    answer.extend([a,b,c])

print(cnt)
print(' '.join(map(str, answer)))