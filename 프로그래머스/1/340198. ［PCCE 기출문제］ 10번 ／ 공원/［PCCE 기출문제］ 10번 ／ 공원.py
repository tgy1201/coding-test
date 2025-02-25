def solution(mats, park):
    row = len(park[0])
    col = len(park)
    
    answer = 0
    m = []
    cnt = 0
    check = 0
    for i in range(col):
        for j in range(row):
            if(park[i][j]=="-1"):
                cnt = 1
                while(1):
                    check = 0
                    for x in range(cnt+1):
                        for y in range(cnt+1):
                            if i+x >= col or j+y >= row or park[i+x][j+y] != "-1":
                                check = 1
                                break
                        if check == 1:
                            break
                    if check == 0:
                        cnt += 1
                    else:
                        break
                m.append(cnt)
                cnt = 0
    mats = list(filter(lambda x : max(m) >= x, mats))        
    if(len(mats) == 0):
        return -1
    return max(mats)