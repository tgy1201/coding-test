m, n = map(int, input().split())
arr = [0] * m
x = 0

str = ""

for a in range(1, m+1):
    arr[a-1] = a

for b in range(1, n+1):
    i, j = map(int, input().split())
    count = 0
    for d in range(i, j+1):
        if (i+j)/2 > d:
            count += 1
            x = arr[d-1]
            arr[d-1] = arr[j-count]
            arr[j-count] = x

for c in arr:
    str += f"{c} "

print(str)