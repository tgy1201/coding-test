def solution(babbling):
    cnt = 0
    test = []
    for i in babbling:
        index = 0
        while True:
            if len(i) == 0:
                cnt += 1
                break
    
            if len(i) == 1:
                break
            if i[index:index+2] == "ye" or i[index:index+2] == "ma":
                i = i[index+2:]
                continue
            
            if len(i) == 2:
                break
            if i[index:index+3] == "woo" or i[index:index+3] == "aya":
                i = i[index+3:]
                continue
            break
    return cnt