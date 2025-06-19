import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

if N >= K:
    print(N-K)
else:
    hq = [(0, N)]
    temp = [1e9]*(K+2)
    temp[N] = 0

    while hq:
        depth, c = heapq.heappop(hq)
        if c == K:
            break

        for i in [c-1, c+1, c*2]:
            if 0 <= i <= K+1:
                if i == c*2 and temp[i] > depth:
                    temp[i] = depth
                    heapq.heappush(hq, (depth, i))
                elif i != c*2 and temp[i] > depth+1:
                    temp[i] = depth + 1
                    heapq.heappush(hq, (depth+1, i))

    print(temp[K])