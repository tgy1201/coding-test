import sys

N, K = map(int, input().split())

li = []

for i in range(N):
    li.append(int(input()))

li.reverse()

cnt = 0
answer = 0
while K != 0:
    answer += K//li[cnt]
    K %= li[cnt]
    cnt += 1

print(answer)