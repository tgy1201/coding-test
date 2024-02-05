import sys

n = int(sys.stdin.readline())
arr = [] * n
av = round(n * 0.15 + 0.0000001)
cnt = 0
for x in range(0, n):
    k = int(sys.stdin.readline())
    arr.append(k)
arr = sorted(arr)

for x in range(av, n-av):
    cnt += arr[x]
if n!= 0:
    print(round(cnt/(n-2*av)+0.0000001))
else:
    print(0)