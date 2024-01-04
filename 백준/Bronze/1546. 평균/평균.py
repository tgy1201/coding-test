m = int(input())
arr = list(map(int, input().split()))
max = -1
a = 0
avg = 0.0

for i in arr:
    if i > max:
        max = i

for j in arr:
    a = float(j/max*100)
    avg += a

avg = avg/m
print(avg)