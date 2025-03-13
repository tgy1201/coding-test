def solution(progresses, speeds):
    answer = [0] * len(progresses)
    dd = []
    
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            answer[i] = (100-progresses[i]) // speeds[i]
        else:
            answer[i] = int((100-progresses[i]) // speeds[i])+1
    
    dd.append(answer[0])
    cc = []
    cnt = 1
    for i in range(1, len(answer)):
        if dd[-1] >= answer[i]:
            cnt += 1
        else:
            dd.append(answer[i])
            cc.append(cnt)
            cnt = 1
    cc.append(cnt)
    return cc