from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [] * (N+1)
dp.append(A[0])

for i in range(1, N):
    if dp[-1] < A[i]:
        dp.append(A[i])
    else:
        index = bisect_left(dp, A[i])
        dp[index] = A[i]

print(len(dp))
