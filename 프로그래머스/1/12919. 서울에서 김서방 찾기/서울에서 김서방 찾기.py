def solution(seoul):
    cnt = 0
    for i in range(len(seoul)):
        if(seoul[i] == "Kim"):
            cnt = i
            break
    str = f"김서방은 {cnt}에 있다"
    return str