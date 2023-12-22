arr2 = []
arr3 = []
max = 0
min = 31

for a in range(1,29):
    i = int(input())
    arr2.append(i)

for b in range(1,31):
    if b not in arr2:
        arr3.append(b)

for c in arr3:
    if c > max:
        max = c
    if c < min:
        min = c

print(min)
print(max)