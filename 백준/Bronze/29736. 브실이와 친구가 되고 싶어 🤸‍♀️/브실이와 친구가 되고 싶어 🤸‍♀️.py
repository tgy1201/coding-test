import sys
input = sys.stdin.readline

a, b = map(int, input().split())
k, x = map(int, input().split())

aa = max(a, k - x)
bb = min(b, k + x)

answer = bb - aa + 1

if answer <= 0:
    print('IMPOSSIBLE')
else:
    print(answer)