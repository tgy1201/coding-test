a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
cnt = 0
for x in range(0, 10):
    for y in range(0, len(d)):
        if str(x) == d[y]:
            cnt = cnt + 1
    print(cnt)
    cnt = 0
    