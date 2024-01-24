a, b = map(int, input().split())
c = int(input())
n = int(input())
cnt = 0

for x in range(n, 101):
    if b > x*(c-a):
        cnt = cnt + 1
        break

if cnt == 0:
    print(1)
else:
    print(0)