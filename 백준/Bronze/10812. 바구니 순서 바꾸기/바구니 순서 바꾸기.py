import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = [i+1 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    start = li[i-1:k-1]
    end = li[k-1:j]

    li[i-1:j] = end+start

print(' '.join(map(str, li)))