s = input()

li = [0] * 10

for i in range(len(li)):
    print(i, end=' ')
print()

for i in s:
    li[int(i)] += 1

for i in li:
    print(i, end=' ')