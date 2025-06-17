from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    e = list(map(int, input().split()))

    li.append(e)

answer = [[0]*(i+1) for i in range(N)]
answer[0][0] = li[0][0]

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            answer[i][j] = li[i][j] + answer[i-1][j]
        elif j == i:
            answer[i][j] = li[i][j] + answer[i-1][j-1]
        else:
            answer[i][j] = max(answer[i-1][j]+li[i][j], answer[i-1][j-1]+li[i][j])

print(max(answer[N-1]))