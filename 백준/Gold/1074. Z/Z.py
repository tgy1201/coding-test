import sys

input = sys.stdin.readline
n, c, r = map(int, input().split())
N = pow(2, n)
cnt = 0
result = 0

def calc(x,y,s):
    global cnt, result

    if s == 1:
        if x == c and y == r:
            result = cnt
        cnt += 1
        return

    if c < x+s//2 and r < y+s//2:
        calc(x, y, s//2)
    elif c < x+s//2 and r >= y+s//2:
        cnt += pow(s//2, 2)
        calc(x, y + s // 2, s // 2)
    elif c >= x+s//2 and r < y+s//2:
        cnt += 2*(pow(s//2, 2))
        calc(x + s // 2, y, s // 2)
    else:
        cnt += 3 * (pow(s // 2, 2))
        calc(x+s//2, y+s//2, s//2)

calc(0, 0, N)

print(result)