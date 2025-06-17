import sys
input = sys.stdin.readline

N, M = map(int, input().split())

li = []
temp = [[0]*N for _ in range(N)]

for _ in range(N):
    e = list(map(int, input().split()))

    li.append(e)

temp[0][0] = li[0][0]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        if i == 0:
            temp[i][j] = temp[i][j-1] + li[i][j]
        elif j == 0:
            temp[i][j] = temp[i-1][j] + li[i][j]
        else:
            temp[i][j] = temp[i-1][j]+temp[i][j-1]-temp[i-1][j-1]+li[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    answer = 0
    if x1 == 0 and y1 == 0:
        answer = temp[x2][y2]
    elif x1 == 0:
        answer = temp[x2][y2] - temp[x2][y1 - 1]
    elif y1 == 0:
        answer = temp[x2][y2] - temp[x1 - 1][y2]
    else:
        answer = temp[x2][y2]-temp[x1-1][y2]-temp[x2][y1-1]+temp[x1-1][y1-1]

    print(answer)


