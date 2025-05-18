T = int(input())

for i in range(T):
    N = int(input())
    
    li = [["0"]*N for _ in range(N)]
    
    di = [[0,1], [1,0], [0,-1], [-1,0]]
    col, row = 0, 0
    cur = 0
    for j in range(N**2):
        li[col][row] = str(j+1)
        
        if 0 <= col+di[cur%4][0] < len(li) and 0 <= row+di[cur%4][1] < len(li[0]) and li[col+di[cur%4][0]][row+di[cur%4][1]] == "0":
            col += di[cur%4][0]
            row += di[cur%4][1]
        else:
            cur += 1
            col += di[cur%4][0]
            row += di[cur%4][1]
    print(f"#{i+1}")
    for j in li:
        print(" ".join(j))