import sys
N = int(sys.stdin.readline())

temp = [0] * (N+1)
temp[1] = 1

for i in range(2, N+1):
    cnt = 1e9
    for j in range(1, int(i**0.5)+1):
        cnt = min(cnt, 1+temp[i-(j**2)])
    temp[i] = cnt

print(temp[N])