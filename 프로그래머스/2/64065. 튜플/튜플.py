from collections import Counter
def solution(s):
    temp = ""
    dd = []
    cnt = 0
    for i in s[1:len(s)-1]:
        if i != "{" and i != "}":
            temp += i
    dd = list(map(int, temp.split(',')))
    ss = Counter(dd)
    
    answer = [0] * len(ss)
    
    for i in sorted(ss):
        answer[int(ss[i])-1] = i
    answer.reverse()
    return answer