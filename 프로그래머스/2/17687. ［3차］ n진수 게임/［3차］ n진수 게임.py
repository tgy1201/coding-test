def solution(n, t, m, p):
    answer = []
    test = ""
    cnt = 0
    while cnt < t*m:
        answer.extend(conv(cnt,n))
        cnt += 1
    
    check = 0
    for i in answer[p-1::m]:
        if(check >= t):
            break
        test += str(i)
        check +=1
    return test
def conv(num, n):
    dd = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    a = []
    while True:
        if(num < n):
            if(num >= 10):
                a.append(dd[num])
            else:
                a.append(num)
            break
        b = num % n
        num //= n
        if(b >= 10):
            a.append(dd[b])
        else:
            a.append(b)
    a.reverse()
    return a