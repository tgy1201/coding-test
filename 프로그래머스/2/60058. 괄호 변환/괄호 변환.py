def solution(p):
    return cal(p)
    
def cal(p): 
    if len(p) == 0:
        return ''
    
    ui = 1001
    aa = []
    a= 0 #(
    b= 0 #)
    for i in range(len(p)):
        if len(aa) == 0:
            aa.append(p[i])
            if p[i] == "(":
                a +=1
            else:
                b +=1
        else:
            if p[i] == "(":
                a +=1
                aa.append(p[i])
            else:
                b +=1
                if aa[-1] == "(":
                    aa.pop()
                else:
                    aa.append(p[i])
        
        if a == b and ui > i:
            ui = i
    if len(aa) == 0:
        return p

    if correct(p[:ui+1]):
        return p[:ui+1] + cal(p[ui+1:])
    else:
        return "("+cal(p[ui+1:])+")"+rev(p[:ui+1])
def correct(s):
    aa = []
    for i in range(len(s)):
        if len(aa) == 0:
            aa.append(s[i])
        else:
            if s[i] == ")" and aa[-1] == "(":
                aa.pop()
            else:
                aa.append(s[i])
    if len(aa) == 0:
        return True
    else:
        return False
            
    
def rev(s):
    s = s[1:len(s)-1]
    t = []
    for i in s:
        if i == "(":
            t.append(")")
        else:
            t.append("(")
    return ''.join(t)