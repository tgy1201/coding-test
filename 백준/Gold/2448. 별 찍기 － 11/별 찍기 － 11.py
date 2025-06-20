import sys

input = sys.stdin.readline

N = int(input())

star = [[" "]*(N*2+1) for _ in range(N)]

star[0][N] = "*"

for i in range(1, N):
    start = 0
    end = 0

    flag = 0 # 빈칸/별
    for j in range(0, N*2+1):
        if i%3 == 1:
            if star[i-1][j] == "*":
                star[i][j-1] = "*"
                star[i][j+1] = "*"
        elif i%3 == 2:
            if star[i-1][j] == "*":
                star[i][j - 1] = "*"
                star[i][j] = "*"
                star[i][j + 1] = "*"
        else:
            if star[i-1][j] != "*":
                if flag == 0:
                    start += 1
                else:
                    end += 1

                if end >= 2:
                    end = 0
                    star[i][j-1] = "*"
                    flag = 0

            else:
                end = 0
                if start >= 2:
                    start = 0
                    star[i][j-1] = "*"
                    flag = 1

    print(''.join(star[i-1][1:]))
print(''.join(star[N-1][1:]))

