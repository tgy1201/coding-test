a = input()
b = a.upper()
count = 0
ans = -1
max = -1

arr = [0]*len(b)

for x in set(b):
    arr.append(b.count(x))
    if max < b.count(x):
        max = b.count(x)
        ans = x
    elif b.count(x) == max:
        ans = '?'

print(ans)