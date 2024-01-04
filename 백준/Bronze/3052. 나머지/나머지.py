arr = []

for a in range(1,11):
    i = int(input())
    j = i%42
    if j not in arr:
        arr.append(j)

print(len(arr))