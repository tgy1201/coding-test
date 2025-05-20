T = int(input())

def dfs(row, col):
    if len(col) == N:
        return 1
    cnt = 0
    for i in range(N):
        if i in col:
            continue
        check = 0
        for index, j in enumerate(col):
            if abs(j-i) == abs(index-row-1):
                check = 1
                break
        if check == 1:
            continue
        col.append(i)
        cnt += dfs(row+1, col)
        col.remove(i)
    return cnt
        
    

for i in range(T):
    N = int(input())
    answer = 0
    
    for j in range(N):
        answer += dfs(0, [j])
        
    print(f"#{i+1} {answer}")