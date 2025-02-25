def solution(schedules, timelogs, startday):
    week = [0, 1, 1, 1, 1, 1, 0] #일~토
    cnt = 0
    
    for i in range(len(schedules)):
        ss = caltime(schedules[i])
        check = 0
        for index, j in enumerate(timelogs[i]):
            ww = week[(index + startday) % 7]
            tt = caltime(j)
            
            if(ww == 0):
                continue
            
            if (ss+10 < tt):
                check = 1
                break
        if(check == 0):
            cnt +=1
            
    return cnt

def caltime(i):
    a = i // 100 #시
    b = i % 100 #분
    
    return a*60 + b