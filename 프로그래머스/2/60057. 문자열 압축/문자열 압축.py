def solution(s):
    answer = len(s)
    test = []
    for i in range(1, len(s)):
        current = ""
        key = ""
        
        dup = []
        cnt = 0
        for j in range(0, len(s)//i*i, i):
            current = s[j:j+i]
            
            if current == key:
                cnt += 1
            else:
                key = current
                if cnt != 0:
                    dup.append(cnt)
                cnt = 0
            if j == len(s)//i*i-i and cnt != 0:
                dup.append(cnt)
                

        ccnt = 0
        for j in dup:
            if j >= 999:
                ccnt += j * i - 4
            elif j >= 99:
                ccnt += j * i - 3
            elif j >= 9:
                ccnt += j * i - 2
            else:
                ccnt += j * i - 1

        if answer > len(s) - ccnt:
            answer = len(s) - ccnt
            
    return answer