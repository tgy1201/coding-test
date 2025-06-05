import sys
import heapq
input = sys.stdin.readline
N = int(input())

li = []
for _ in range(N):
    num = int(input())

    if num == 0:
        if len(li) == 0:
            print(0)
        else:
            print(-heapq.heappop(li))
    else:
        heapq.heappush(li, -num)
