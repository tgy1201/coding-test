import copy
def solution(m, n, board):
    answer = 0
    bb = []
    
    for i in range(n):
        s = []
        for j in range(m):
            s.append(board[m-j-1][i])
        bb.append(s)

    def cal(b, cnt):
        a = copy.deepcopy(b)
        dx = [0, 1, 1]
        dy = [1, 0, 1]
        
        for i in range(len(b)):
            if(len(b[i])== 0):
                continue
            for j in range(len(b[i])):
                check = 0
                for k in range(3):
                    x = i + dx[k]
                    y = j + dy[k]
                    
                    if x >= len(b) or y >= len(b[i]):
                        check = 1
                        break
                    
                    if(b[i][j] != b[x][y] or b[i][j] == "1"):
                        check = 1
                        break
                if(check == 0):
                    a[i][j], a[i+1][j], a[i][j+1], a[i+1][j+1] = "0", "0", "0", "0"
        c = []
        count = 0

        for i in a:
            s = []
            h = 0
            for j in i:
                if j == "0":
                    h += 1
                else:
                    s.append(j)
            s.extend("1"*h)
            count += h
            c.append(s)
        cnt += count

        if(count == 0):
            return cnt
        return cal(c, cnt)
    return cal(bb, answer)