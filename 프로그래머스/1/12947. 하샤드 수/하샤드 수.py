def solution(x):
    l = list(str(x))
    m = [int(i) for i in l]
    cnt = sum(m)
    
    if(x % cnt == 0):
        return True
    else:
        return False