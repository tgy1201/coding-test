n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
max = -1

for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            cnt = arr[x] + arr[y] + arr[z]
            if m >= cnt and cnt >= max:
                max = cnt

print(max)
