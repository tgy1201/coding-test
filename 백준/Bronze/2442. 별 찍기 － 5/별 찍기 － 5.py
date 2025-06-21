import sys, copy

input = sys.stdin.readline

N = int(input())

star = [[" "]*(N*2) for _ in range(N)]
star[0][N-1] = "*"

for i in range(1, N):
    for j in range(N*2):
        if star[i-1][j] == "*":
            star[i][j-1] ="*"
            star[i][j] = "*"
            star[i][j+1] = "*"

for i in range(N):
    cnt = 0
    for j in range(N*2):
        if star[i][j] == "*":
            cnt += 1
        print(star[i][j], end="")

        if cnt == 2*(i+1)-1:
            break
    print()
