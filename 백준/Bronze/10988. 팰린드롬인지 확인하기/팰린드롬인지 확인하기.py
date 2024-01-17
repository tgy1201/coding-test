a = input()
b = len(a) // 2
count = 1

for x in range(b):
    if a[x] != a[len(a)-x-1]:
        count = 0

print(count)