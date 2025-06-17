from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

li = []

for k in range(N):
    e = list(map(int, input().split()))
    if k == 0:
        li = e[:]
    else:
        for index, i in enumerate(e):
            x = 1e9
            for j in range(len(li)):
                if index != j:
                    x = min(x, li[j]+i)
            e[index] = x
        li = e[:]
print(min(li))




