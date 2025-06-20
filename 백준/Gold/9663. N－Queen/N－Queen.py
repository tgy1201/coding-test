import sys
from collections import deque
sys.setrecursionlimit(10**4)

N = int(input())

answer = 0

def queen(x, y):
    global answer

    if x == N-1:
        answer += 1
        return

    for i in range(N):
        xx = x+1
        yy = i

        check = 0
        for col, row in enumerate(visited):
            if yy == row or abs(xx-col) == abs(yy-row):
                check = 1
                break
        if check == 1:
            continue
        visited.append(yy)
        queen(xx, yy)
        visited.pop()


for i in range(N):
    visited = deque([i])
    queen(0, i)

print(answer)