def solution(s):
    cnt = len(s)//2
    if(len(s) % 2 != 0):
        answer = s[cnt]
    else:
        answer = s[cnt-1] + s[cnt]
    return answer