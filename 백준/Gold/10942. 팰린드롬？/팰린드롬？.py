import sys
input = sys.stdin.readline

N = int(input())
temp = [[0]*N for _ in range(N)]
li = list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(N-i+1):
        if i == 1:
            temp[j][j] = 1
        else:
            s = j
            e = j + i-1

            if li[s] == li[e]:
                if i == 2:
                    temp[s][e] = 1
                elif temp[s+1][e-1] == 1:
                    temp[s][e] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())

    print(temp[S-1][E-1])
