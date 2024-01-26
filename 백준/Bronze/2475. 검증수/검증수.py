arr = list(map(int, input().split()))
cnt = 0
for x in arr:
    cnt = cnt + x**2

print(cnt % 10)