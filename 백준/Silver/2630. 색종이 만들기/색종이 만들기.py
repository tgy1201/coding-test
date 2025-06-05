import sys
input = sys.stdin.readline
N = int(input())

li = []

for _ in range(N):
    e = list(map(int, input().split()))
    li.append(e)

b = 0
w = 0

def calc(x,y, n):
    global b
    global w
    check = li[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != li[i][j]:
                calc(x,y, n//2)
                calc(x,y+n//2, n//2)
                calc(x+n//2, y, n//2)
                calc(x+n//2, y+n//2, n//2)

                return

    if check == 1:
        b += 1
    else:
        w += 1
calc(0,0,N)
print(w)
print(b)