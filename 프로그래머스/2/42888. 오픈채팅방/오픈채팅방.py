def solution(record):
    answer = []
    dd = {}
    act = []
    
    for i in record:
        a = list(map(str, i.split()))
        
        if a[0] == "Enter":
            act.append([a[0], a[1]])
            dd[a[1]] = a[2]
        elif a[0] == "Leave":
            act.append([a[0], a[1]])
        else:
            dd[a[1]] = a[2]
            
    for i in act:
        s = ""
        if i[0] == "Enter":
            s = f"{dd[i[1]]}님이 들어왔습니다."
        else:
            s = f"{dd[i[1]]}님이 나갔습니다."
        answer.append(s)
        
    return answer