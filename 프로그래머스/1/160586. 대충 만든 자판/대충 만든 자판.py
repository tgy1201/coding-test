def solution(keymap, targets):
    answer = []
    b = 0
    for i in targets:
        cnt = 0
        b = 0
        for j in i:
            m = 101
            for k in keymap:
                if(k.find(j) == -1):
                    continue
                m = min(m, k.find(j))
            if(m == 101):
                b = 1
                break
            cnt += m + 1
        if(b == 1):
            answer.append(-1)
        else:
            answer.append(cnt)
    return answer