import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())

    li = []
    ll = []
    dd = defaultdict(int)

    d = 0
    for j in range(k):
        s, n = map(str, input().strip().split())

        n = int(n)
        if s == "I":
            heapq.heappush(li, n)
            heapq.heappush(ll, -n)
            dd[n] += 1
        else:
            if n == -1:
                while li:
                    x = heapq.heappop(li)
                    if dd[x] > 0:
                        dd[x] -= 1
                        break
            else:
                while ll:
                    x = -heapq.heappop(ll)
                    if dd[x] > 0:
                        dd[x] -= 1
                        break

    min_val, max_val = None, None

    while li:
        x = heapq.heappop(li)
        if dd[x] > 0:
            min_val = x
            break

    while ll:
        x = -heapq.heappop(ll)
        if dd[x] > 0:
            max_val = x
            break

    if min_val is None or max_val is None:
        print("EMPTY")
    else:
        print(f"{max_val} {min_val}")