import sys
input = sys.stdin.readline

AN = int(input())
A = list(map(int, input().strip().split()))
BN = int(input())
B = list(map(int, input().strip().split()))

li = [[[]]*(AN+1) for _ in range(BN+1)]

for i in range(1, BN+1):
    for j in range(1, AN+1):
        if B[i-1] == A[j-1]:
            li[i][j] = li[i-1][j-1][:]

            if not li[i][j]:
                li[i][j].append(A[j-1])
                continue

            if li[i][j][-1] >= A[j-1]:
                li[i][j].append(A[j-1])
            else:
                while li[i][j] and li[i][j][-1] < A[j-1]:
                    li[i][j].pop()
                li[i][j].append(A[j-1])
        else:
            if not li[i-1][j] and not li[i][j-1]:
                continue

            x = len(li[i-1][j])
            y = len(li[i][j-1])

            check = 0
            for k in range(min(x, y)):
                if li[i-1][j][k] < li[i][j-1][k]:
                    check = 1
                    break
                elif li[i-1][j][k] > li[i][j-1][k]:
                    check = 2
                    break

            if check == 0:
                if x > y:
                    li[i][j] = li[i-1][j][:]
                else:
                    li[i][j] = li[i][j - 1][:]
            elif check == 1:
                li[i][j] = li[i][j - 1][:]
            else:
                li[i][j] = li[i-1][j][:]

if li[BN][AN]:
    print(len(li[BN][AN]))
    print(' '.join(map(str, li[BN][AN])))
else:
    print(0)