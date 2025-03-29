def solution(s):
    answer = ''
    start = 0
    
    for i in range(len(s)):
        if(s[i] == " "):
            start = 0
            answer += " "
        else:
            if(start % 2 == 0):
                answer += s[i].upper()
            elif(start % 2 != 0):
                answer += s[i].lower()
            start += 1

    return answer