import sys
from bisect import bisect_left

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = A[::-1]

def lis(b):
    l = [b[0]]
    li = [1]

    for i in range(1, len(b)):
        if l[-1] < b[i]:
            l.append(b[i])
        else:
            index = bisect_left(l, b[i])
            l[index] = b[i]
        li.append(len(l))
    return li


a = lis(A)
b = lis(B)[::-1]

answer= 0
for i in range(N):
    answer = max(answer, a[i]+b[i]-1)
print(answer)