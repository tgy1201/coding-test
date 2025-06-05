import sys
from bisect import bisect_left
input = sys.stdin.readline
N, M = map(int, input().split())

tree = list(map(int, input().split()))
tree.sort()

temp = [0] * (len(tree)+1)
temp[1] = tree[0]
for i in range(2, len(tree)+1):
    temp[i] = temp[i-1] + tree[i-1]

start = 0
end = tree[-1]
mid = (start+end)//2

answer = 0

while start+1 != end:
    index = bisect_left(tree, mid)

    tot = temp[-1] - temp[index] - (len(tree)-index) * mid

    if tot > M:
        answer = max(answer, mid)
        start = mid
    elif tot < M:
        end = mid
    else:
        answer = mid
        break
    mid = (start + end) // 2

print(answer)