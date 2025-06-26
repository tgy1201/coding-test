import sys

input = sys.stdin.readline

li = []
blank = []
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
are = [set() for _ in range(9)]

for i in range(9):
    temp = []
    e = input().strip()

    for index, k in enumerate(e):
        t = int(k)
        if t == 0:
            blank.append((i, index))
        else:
            row[i].add(t)
            col[index].add(t)
            are[(i//3) * 3 + (index//3)].add(t)
        temp.append(t)

    li.append(temp)

def sudoku(index):
    if index == len(blank):
        for i in li:
            print(''.join(map(str, i)))
        sys.exit(0)

    i, j = blank[index]
    
    a = i//3
    b = j//3
    for k in range(1, 10):
        if k not in row[i] and k not in col[j] and k not in are[a*3+b]:
            li[i][j] = k
            row[i].add(k)
            col[j].add(k)
            are[a*3+b].add(k)

            sudoku(index+1)

            row[i].remove(k)
            col[j].remove(k)
            are[a*3+b].remove(k)
            li[i][j] = 0

sudoku(0)
