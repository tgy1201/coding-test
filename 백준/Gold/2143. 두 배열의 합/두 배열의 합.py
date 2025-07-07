import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

answer = 0
dd = defaultdict(int)

for i in range(N):
    cnt = A[i]
    dd[T-cnt] += 1
    for j in range(i+1, N):
        cnt += A[j]
        dd[T-cnt] += 1

for i in range(M):
    cnt = B[i]
    answer += dd[cnt]
    for j in range(i+1, M):
        cnt += B[j]
        answer += dd[cnt]

print(answer)
