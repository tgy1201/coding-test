import sys

N, M = map(int, input().split())
d = set()
answer = []

for i in range(N+M):
    s = sys.stdin.readline().strip()

    if s in d:
        answer.append(s)
    else:
        d.add(s)

answer.sort()
print(len(answer))
for i in answer:
    print(i)