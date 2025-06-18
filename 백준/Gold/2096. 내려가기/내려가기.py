import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))
ll = li[:]
dd = deque()
for _ in range(1, N):
    e = list(map(int, input().split()))

    temp = []
    temp2 = []
    for index, i in enumerate(e):
        ma = 0
        mi = 1e9
        if index == 0:
            for j in range(2):
                ma = max(ma, i+li[j])
                mi = min(mi, i+ll[j])
        elif index == 2:
            for j in range(1,3):
                ma = max(ma, i + li[j])
                mi = min(mi, i + ll[j])
        else:
            for j in range(3):
                ma = max(ma, i + li[j])
                mi = min(mi, i + ll[j])
        temp.append(ma)
        temp2.append(mi)
    li = temp[:]
    ll = temp2[:]

print(f"{max(li)} {min(ll)}")
