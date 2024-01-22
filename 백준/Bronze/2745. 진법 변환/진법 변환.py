a, b = map(str, input().split())
str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0
arr = [0] * len(a)

for x in range(0, len(a)):
    if a[x] in str:
        arr[x] = str.index(a[x])+10
    else:
        arr[x] = int(a[x])
    cnt = cnt + arr[x] * (int(b) ** (len(a)-x-1))
print(cnt)