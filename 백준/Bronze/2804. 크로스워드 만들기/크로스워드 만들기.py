import sys
input = sys.stdin.readline

a, b = map(str, input().strip().split())

x, y = 0, 0
check = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            x = i
            y = j
            check = 1
            break
    if check == 1:
        break

li = [["."]*len(a) for _ in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if i == y:
            li[i][j] = a[j]
        if j == x:
            li[i][j] = b[i]
    print(''.join(li[i]))