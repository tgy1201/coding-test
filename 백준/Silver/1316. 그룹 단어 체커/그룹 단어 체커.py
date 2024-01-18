a = int(input())
cnt = 0

for x in range(a):
    b = input()
    key = [] * 100
    for y in range(1, len(b)):
        if b[y] != b[y-1]:
            key.append(b[y-1])
        if b[y] in key:
            cnt = cnt + 1
            break
print(a-cnt)