import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dd = defaultdict(lambda: [".", "."])
dq = deque()
data = []

def tree(x):
    if dd[x][0] != ".":
        tree(dd[x][0])
    if dd[x][1] != ".":
        tree(dd[x][1])
    print(x)

while True:
    line = input()
    if not line:
        break
    data.append(int(line.strip()))

n = data[0]
dd[n] = [".","."]
dq.append(n)

for a in data[1:]:
    if dq[-1] > a:
        dd[dq[-1]][0] = a
        dq.append(a)
    else:
        x = dq[-1]
        while dq:
            x = dq.pop()
            if not dq or dq[-1] > a:
                break
        dd[x][1] = a
        dq.append(a)

tree(n)