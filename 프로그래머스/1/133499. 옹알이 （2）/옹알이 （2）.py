def solution(babbling):
    data = ""
    b = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for i in babbling:
        data = ""
        while(1):
            s = 0
            if(len(i)==0):
                cnt+=1
                break
            if(len(i)==1):
                break
            if(i[:2]=="ye" or i[:2]=="ma"):
                if(i[:2] == data):
                    break
                data = i[:2]
                i=i[2:]
                s = 1
            if(len(i)==2 and s==0):
                break
            if(i[:3]=="aya" or i[:3]=="woo"):
                if(i[:3] == data):
                    break
                data = i[:3]
                i = i[3:]
                s = 1
            if(s==0):
                break
    return cnt