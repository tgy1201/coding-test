import sys, heapq

N = int(sys.stdin.readline())

hq = []
for _ in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(hq) == 0:
            print(0)
        else:
            x = heapq.heappop(hq)
            print(x)
    else:
        heapq.heappush(hq, n)