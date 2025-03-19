from collections import defaultdict

def solution(n):
    answer = []
    dd = defaultdict(list)

    s = n * (n + 1) // 2

    row, col, num = 0, 0, 1
    direction = 0 
    drow = [1, 0, -1]
    dcol = [0, 1, -1]

    triangle = [[0] * (i + 1) for i in range(n)]

    while num <= s:
        triangle[row][col] = num
        num += 1

        # 다음 위치 계산
        next_row = row + drow[direction]
        next_col = col + dcol[direction]

        # 경계를 벗어나거나 이미 채워진 곳이면 방향 전환
        if next_row >= n or next_col >= len(triangle[next_row]) or triangle[next_row][next_col] != 0:
            direction = (direction + 1) % 3
            next_row = row + drow[direction]
            next_col = col + dcol[direction]

        row, col = next_row, next_col

    for i in range(n):
        dd[i] = triangle[i]

    for i in dd:
        answer.extend(dd[i])

    return answer
