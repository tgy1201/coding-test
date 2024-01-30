from collections import deque
import sys

n = int(sys.stdin.readline())
arr = [] * n
                                              
for x in range(0, n):
    arr.append(x+1)
qq = deque()
qq.extend(arr)

for x in range(0, n):
    if len(qq) == 1:
        break
    qq.popleft()
    qq.append(qq[0])
    qq.popleft()
print(qq[0])