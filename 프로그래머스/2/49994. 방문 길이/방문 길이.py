def solution(dirs):
    dd = {"U": [0,1], "D": [0,-1], "R": [1,0], "L": [-1,0]}
    ss = {"U": "D", "D": "U", "R": "L", "L": "R"}
    
    temp = []
    x, y = 0, 0
    answer = 0
    
    for i in dirs:
        if x+dd[i][0] > 5 or x+dd[i][0] < -5 or y+dd[i][1] > 5 or y+dd[i][1] < -5:
            continue
        temp.append([x,y,i])
        x += dd[i][0]
        y += dd[i][1]
        
        if [x,y,ss[i]] in temp:
            continue
        else:
            answer += 1
            temp.append([x,y,ss[i]])
    return answer