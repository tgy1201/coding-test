import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    li = []
    for _ in range(2):
        e = list(map(int, input().split()))
        li.append(e)

    temp = [[0]*n for _ in range(2)]

    if n == 1:
        print(max(li[0][0], li[1][0]))
    else:
        temp[0][0] = li[0][0]
        temp[1][0] = li[1][0]
        temp[0][1] = temp[1][0]+li[0][1]
        temp[1][1] = temp[0][0]+li[1][1]

        for i in range(2, n):
            temp[0][i] = max(temp[0][i-2], temp[1][i-2], temp[1][i-1]) + li[0][i]
            temp[1][i] = max(temp[0][i-2], temp[1][i-2], temp[0][i-1]) + li[1][i]

        print(max(temp[0][n-1], temp[1][n-1], temp[0][n-2], temp[1][n-2]))

