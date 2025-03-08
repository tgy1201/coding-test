from collections import deque
def solution(n):
    answer = 0
    
    for i in range(n):
        col = [i]
        answer += dfs(0, col, n)
        
    return answer

def dfs(row, col, n):
    if(len(col) == n):
        return 1
    count = 0
    for i in range(n):
        if i in col:
            continue
        check = 0
        for index, j in enumerate(col):
            if abs(row + 1 - index) == abs(i - j):
                check = 1
                break
        if check == 1:
            continue
        col.append(i)
        count += dfs(row+1, col, n)
        col.remove(i)
    return count
    
    