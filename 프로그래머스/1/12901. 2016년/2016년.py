def solution(a, b):
    cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = ''
    mon = 0
    for i in range(1, a):
        mon += cal[i-1]
    
    cnt = (mon+b) % 7
    
    if(cnt == 1):
        answer = "FRI"
    elif(cnt == 2):
        answer = "SAT"
    elif(cnt == 3):
        answer = "SUN"
    elif(cnt == 4):
        answer = "MON"
    elif(cnt == 5):
        answer = "TUE"
    elif(cnt == 6):
        answer = "WED"
    elif(cnt == 0):
        answer = "THU"
    return answer