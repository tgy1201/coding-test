import sys
N, M = map(int, input().split())

dd = {}
for i in range(N):
    s, b = map(str, sys.stdin.readline().strip().split())
    dd[s] = b

for i in range(M):
    ss = sys.stdin.readline().strip()

    print(dd[ss])