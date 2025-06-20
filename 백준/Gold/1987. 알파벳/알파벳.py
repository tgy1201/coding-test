import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = []
for _ in range(R):
    e = input().strip()

    temp = []
    for i in e:
        temp.append(i)
    board.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

def dfs(x, y):
    global answer
    answer = max(answer, len(visited))

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < R and 0 <= yy < C and board[xx][yy] not in visited:
            visited.add(board[xx][yy])
            dfs(xx, yy)
            visited.remove(board[xx][yy])


visited = set()
visited.add(board[0][0])
dfs(0, 0)

print(answer)