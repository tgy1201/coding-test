import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

li.sort()
answer = 0

for i in range(10001):
    x = bisect_left(li, i)

    if n - x >= i:
        answer = i
    else:
        break
print(answer)