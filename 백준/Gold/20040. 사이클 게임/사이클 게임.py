import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

p = [i for i in range(N)]
answer = 0

def parent(x):
    if x != p[x]:
        return parent(p[x])
    return x

for i in range(M):
    a, b = map(int, input().split())

    aa = parent(a)
    bb = parent(b)

    if aa == bb:
        answer = i+1
        break

    if aa > bb:
        p[aa] = bb
    else:
        p[bb] = aa

print(answer)