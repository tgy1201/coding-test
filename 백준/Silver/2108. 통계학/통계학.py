from collections import Counter
import sys

n = int(sys.stdin.readline())
arr = [] * n
cnt = 0

for x in range(0, n):
    a = int(sys.stdin.readline())
    cnt = cnt + a
    arr.append(a)

arr = sorted(arr)
print(round(cnt / n))
print(arr[len(arr)//2])

cc = Counter(arr).most_common()
if len(cc) > 1 and cc[0][1] == cc[1][1]:
    print(cc[1][0])
else:
    print(cc[0][0])

print(max(arr)-min(arr))