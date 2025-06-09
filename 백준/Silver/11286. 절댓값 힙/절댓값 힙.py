import sys, heapq

input = sys.stdin.readline

N = int(input())
temp = []

for _ in range(N):
    i = int(input())

    if i == 0:
        if len(temp) == 0:
            print(0)
        else:
            x = heapq.heappop(temp)
            print(x[1])
    else:
        heapq.heappush(temp, [abs(i),i])