def solution(s, n):
    answer = ''
    for i in s:
        if(i==" "):
            answer += " "
            continue
        if(ord(i)>=97):
            answer += chr((ord(i)-97+n)%26+97)
        else:
            answer += chr((ord(i)-65+n)%26+65)    
    return answer