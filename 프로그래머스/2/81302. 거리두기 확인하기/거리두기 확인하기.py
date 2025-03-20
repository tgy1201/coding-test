from collections import defaultdict, deque
def solution(places):
    answer = []
    dd = defaultdict(list)
    
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    dd[i].append([j,k])
                    
    for i in range(5):
        if len(dd[i]) == 0:
            answer.append(1)
            continue
        check = 0
        for j in dd[i]:
            if dfs([j[0],j[1],0], places[i]):
                continue
            else:
                check = 1
                answer.append(0)
                break
        if check == 0:
            answer.append(1)
    
    return answer

def dfs(s, p):
    temp = deque()
    temp.append(s)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visit = set()
    visit.add((s[0], s[1]))
    
    while temp:
        a, b, l = temp.popleft()
        
        if l >= 2:
            continue
            
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
        
            if 0 <= xx < 5 and 0 <= yy < 5 and (xx, yy) not in visit:
                if p[xx][yy] == "P":  # 거리 2 이내에서 다른 사람 발견
                    return False
                elif p[xx][yy] == "X":  # 벽이면 이동 불가
                    continue
                
                temp.append((xx, yy, l + 1))
                visit.add((xx, yy))
    return True
            