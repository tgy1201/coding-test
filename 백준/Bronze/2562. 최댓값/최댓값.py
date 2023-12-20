arr = []
count = 0
index = -1
max = -1

for i in range(1, 10):
    n = int(input())
    arr.append(n)

for j in arr:
    count += 1
    if max < j:
        max = j
        index = count
    else:
        pass

print(max)
print(index)