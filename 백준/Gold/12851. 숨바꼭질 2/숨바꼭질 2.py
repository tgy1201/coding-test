import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

temp = [1e9] * (K+2)

if N >= K:
    print(N-K)
    print(1)
else:
    temp[N] = 0

    dq = deque()
    dq.append((N, 0))
    answer = 0
    m = 1e9

    while dq:
        x, dist = dq.popleft()

        if dist > temp[x]:
            continue

        if dist > m:
            break

        if x == K:
            answer += 1
            m = dist

        for i in [x-1, x+1, x*2]:
            if 0 <= i <= K+1 and temp[i] >= dist + 1:
                temp[i] = dist + 1
                dq.append((i, temp[i]))

    print(m)
    print(answer)