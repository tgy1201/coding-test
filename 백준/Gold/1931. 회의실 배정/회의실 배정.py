import sys, heapq

input = sys.stdin.readline

N = int(input())
cnt = 0

li = []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(li, (b,a))

t = 0
while li:
    a = heapq.heappop(li)

    if t <= a[1]:
        cnt += 1
        t = a[0]
print(cnt)