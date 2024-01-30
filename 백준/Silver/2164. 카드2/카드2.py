from collections import deque
import sys

n = int(sys.stdin.readline())
qq = deque()
                                              
for x in range(0, n):
    qq.append(x+1)

for x in range(0, n):
    if len(qq) == 1:
        break
    qq.popleft()
    qq.append(qq[0])
    qq.popleft()
print(qq[0])