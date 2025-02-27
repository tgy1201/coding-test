def solution(land):
    dd = [[0]*4 for _ in range(len(land))]
    dd[0] = land[0]
    
    for i in range(1,len(land)):
        for j in range(4):
            dd[i][j] = max(land[i][j]+dd[i-1][(j+1)%4],land[i][j]+dd[i-1][(j+2)%4],land[i][j]+dd[i-1][(j+3)%4])
    return max(dd[-1])

'''
from collections import deque
def solution(land):
    answer = []
    
    hx = [1, 1, 1]
    hy = [1, 2, 3]
    
    for i in range(4):
        queue = deque()
        queue.append((0,i, land[0][i]))
        
        while queue:
            a, b, point = queue.popleft()
            
            for j in range(3):
                dx = a + hx[j]
                dy = (b + hy[j]) % 4
                
                if 0 > dy or dy >= 4 or dx >= len(land):
                    continue
                queue.append((dx, dy, point+land[dx][dy]))
                if(dx == len(land)-1):
                    answer.append(point+land[dx][dy])
    return max(answer
'''