import sys, copy

input = sys.stdin.readline

R, C, T = map(int, input().split())

house = []
a1 = 0 #공기청정기 몇번쨰 열
virus = set()
mount = 0

for i in range(R):
    e = list(map(int, input().split()))

    for index, j in enumerate(e):
        if j == -1:
            a1 = i
        elif j != 0:
            mount += j
            virus.add((i,index))
    house.append(e)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(T):
    temp = [[0]*C for _ in range(R)]
    temp[a1][0] = -1
    temp[a1-1][0] = -1

    #오염
    new = set()
    for x, y in virus:
        cnt = 0
        m = house[x][y] // 5

        if m != 0:
            for j in range(4):
                xx = x + dx[j]
                yy = y + dy[j]
                if 0 <= xx < R and 0 <= yy < C and house[xx][yy] != - 1:
                    cnt += 1
                    temp[xx][yy] += m

        temp[x][y] += house[x][y] - (m*cnt)

    mount = mount - temp[a1-2][0] - temp[a1+1][0]

    #정화
    x = 0
    for j in range(a1):
        if j == 0:
            x = temp[j].pop(0)
            temp[j].append(temp[j+1][-1])
        elif j != a1-1:
            s = temp[j][0]
            temp[j][0] = x
            x = s
            temp[j][-1] = temp[j+1][-1]
        else:
            temp[j].pop()
            temp[j].insert(1, 0)
    x = 0
    for j in range(a1, R):
        if j == a1:
            x = temp[j].pop()
            temp[j].insert(1, 0)
        elif j != R-1:
            s = temp[j][-1]
            temp[j][-1] = x
            x = s
            temp[j][0] = temp[j+1][0]
        else:
            temp[j].pop(0)
            temp[j].append(x)

    house = copy.deepcopy(temp)

    virus.clear()
    for j in range(R):
        for k in range(C):
            if house[j][k] > 0:
                virus.add((j,k))

print(mount)
