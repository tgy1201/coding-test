import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    e = list(map(int, input().split()))
    li.append(e)

def dfs(start, row):
    temp = []

    if row == N-1:
        for i in range(3):
            m = 1e9
            for index, j in enumerate(current):
                if index != i and i != start:
                    m = min(m, j)

            temp.append(m)

        for i in range(3):
            current[i] = temp[i] + li[row][i]

        return

    for i in range(3):
        m = 1e9
        for index, j in enumerate(current):
            if index != i:
                m = min(m, j)

        temp.append(m)

    for i in range(3):
        current[i] = temp[i] + li[row][i]

    dfs(start, row+1)

answer = []
a, b, c = li[0]
current = [a, 1e9, 1e9]
dfs(0, 1)
answer.extend(current)

current = [1e9, b, 1e9]
dfs(1, 1)
answer.extend(current)

current = [1e9, 1e9, c]
dfs(2, 1)
answer.extend(current)

print(min(answer))