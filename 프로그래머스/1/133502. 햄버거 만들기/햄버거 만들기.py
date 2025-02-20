def solution(ingredient):
    s = "1231"
    d = ''.join(list(map(lambda x: str(x), ingredient)))
    answer = 0
    a = ""
    for i in d:
        a += i
        if(a[-4:] == s):
            a = a[:-4]
            answer +=1
    return answer