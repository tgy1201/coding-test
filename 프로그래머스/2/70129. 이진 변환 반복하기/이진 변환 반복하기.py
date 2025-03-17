def solution(s):
    cnt = 0
    convert = 0
    while s != "1":
        for i in s:
            if i == "0":
                s = s.replace(i, "", 1)
                cnt += 1
        s = bin(len(s))[2:]
        convert += 1
    return [convert, cnt]
    