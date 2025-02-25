from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = deque()
    queue.append((0,0,1))
    maps[0][0] = 2
    check = 0
    
    while queue:
        x, y, depth = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(0 > nx or col <= nx or 0 > ny or row <= ny):
                continue
            if(maps[ny][nx] == 0):
                continue
            
            if(maps[ny][nx] == 1):
                if(nx == col-1 and ny == row-1): #도착지점 도달
                    return depth+1
                maps[ny][nx] += 1
                queue.append((nx,ny, depth+1))
    return -1