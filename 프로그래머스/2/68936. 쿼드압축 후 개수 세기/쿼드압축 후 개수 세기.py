from collections import deque
def solution(arr):
    answer = [0, 0]
    a = len(arr)
    
    def dfs(x, y, a):
        key = arr[x][y]
        check = 0
        for i in range(a):
            for j in range(a):
                if key != arr[x+i][y+j]:
                    check = 1
                    dfs(x, y, a//2)
                    dfs(x+a//2, y, a//2)
                    dfs(x, y+a//2, a//2)
                    dfs(x+a//2, y+a//2, a//2)
                    break
            if check == 1:
                break
        if check == 0:
            if key == 1:
                answer[1] +=1
            else:
                answer[0] += 1
    dfs(0,0,a)
    return answer