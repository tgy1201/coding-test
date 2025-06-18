import sys
from collections import deque
input = sys.stdin.readline

A = input().strip()
B = input().strip()

com = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            com[i][j] = com[i-1][j-1] + 1
        else:
            com[i][j] = max(com[i][j-1], com[i-1][j])

print(max(com[-1]))

