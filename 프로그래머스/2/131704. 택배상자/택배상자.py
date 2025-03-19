def solution(order):
    answer = 0
    temp = [0]
    
    cnt = 0
    
    for i in order:
        if temp[-1] < i:
            while cnt != i:
                cnt += 1
                temp.append(cnt)
            temp.pop()
            answer += 1
        elif temp[-1] == i:
            answer += 1
            temp.pop()
        else:
            break
    return answer