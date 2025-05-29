import math

N = int(input())
S = list(map(int, input().split()))
T, P = map(int, input().split())

cnt = 0
for i in S:
    cnt += math.ceil(i/T)
print(cnt)
print(f"{N//P} {N%P}")