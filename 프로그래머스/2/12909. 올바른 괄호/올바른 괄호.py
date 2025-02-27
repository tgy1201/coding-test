def solution(s):
    queue= []
    
    if(len(s) % 2 != 0 or s[0] == ")"):
        return False
    for i in s:
        if(len(queue) != 0 and queue[-1] == "(" and i == ")"):
            queue.pop()
        else:
            queue.append(i)
    
    if(len(queue) == 0):
        return True
    return False