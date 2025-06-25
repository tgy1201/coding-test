import sys

input = sys.stdin.readline

C, N = map(int, input().split())

temp = [[1e9]*N for _ in range(C+1)]
temp[0][0] = 0
li = []
for _ in range(N):
    cost, p = map(int, input().split())
    li.append((cost, p))

for i in range(1, C+1):
    for j in range(len(li)):
        x, y = li[j]

        if i <= y:
            temp[i][j] = min(temp[i][j-1], x)
        else:
            temp[i][j] = min(temp[i][j-1], min(temp[i-y])+x)
print(temp[C][N-1])