import sys
t = int(sys.stdin.readline())
cnt = 0

for x in range(0, t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    cnt = 0
    arr = [[0 for i in range(n+1)] for j in range(k+1)]

    for y in range(1, n+1):
        arr[0][y] = y

    for z in range(1, k+1):
        for q in range(1, n+1):
            for w in range(1, q+1):
                arr[z][q] = arr[z][q] + arr[z-1][w]
    print(arr[k][n])