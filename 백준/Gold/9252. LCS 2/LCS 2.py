import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()

lcs = [[""]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if B[i-1] == A[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + A[j-1]
        else:
            if len(lcs[i-1][j]) > len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]

print(len(lcs[len(B)][len(A)]))
print(lcs[len(B)][len(A)])
