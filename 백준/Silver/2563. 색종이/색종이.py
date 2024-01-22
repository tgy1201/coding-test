arr = [[0 for col in range(100)] for row in range(100)]
a = int(input())
count = 0

for i in range(a):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            if arr[j][k] == 0:
                arr[j][k] = 1
                count = count + 1

print(count)
