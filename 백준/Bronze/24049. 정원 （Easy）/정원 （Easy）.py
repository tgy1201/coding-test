import sys
input = sys.stdin.readline

N, M = map(int, input().split())

left = list(map(int ,input().split()))
top = list(map(int ,input().split()))

garden = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    garden[i][0] = left[i-1]

for i in range(1, M+1):
    garden[0][i] = top[i-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        if garden[i-1][j] == garden[i][j-1]:
            garden[i][j] = 0
        else:
            garden[i][j] = 1

print(garden[N][M])
