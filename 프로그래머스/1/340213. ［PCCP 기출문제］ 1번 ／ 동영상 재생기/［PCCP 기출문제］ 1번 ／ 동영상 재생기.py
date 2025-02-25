def solution(video_len, pos, op_start, op_end, commands):
    v = caltime(video_len)
    p = caltime(pos)
    os = caltime(op_start)
    oe = caltime(op_end)
    
    if os <= p <= oe:
        p = oe
    
    for i in commands:
        if i=="next":
            p = min(v, p+10)
        else:
            p = max(0, p-10)
            
        if os <= p <= oe:
            p = oe
    
    a = p // 60
    b = p % 60
    
    if(0 < a < 10):
        a = f"0{a}"
    elif(a == 0):
        a = "00"
    
    if(0 < b < 10):
        b = f"0{b}"
    elif(b == 0):
        b = "00"
    s = f"{a}:{b}"
    return s

def caltime(s):
    a, b = map(int, s.split(":"))
    time = a * 60 + b
    
    return time