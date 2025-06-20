import sys

input = sys.stdin.readline

N, B = map(int, input().split())

li = []
for i in range(N):
    e = list(map(int, input().split()))

    li.append(e)

def matrix(l, c):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += l[i][k] * c[k][j]
            temp[i][j] %= 1000
    return temp

def power(m, b):
    if b == 1:
        return mod(m)
    h = power(m, b//2)
    if b%2 ==0:
        return matrix(h, h)
    else:
        return matrix(matrix(h,h),m)

def mod(m):
    for i in range(N):
        for j in range(N):
            m[i][j] %= 1000
    return m

answer = power(li, B)

for i in answer:
    print(' '.join(map(str, i)))