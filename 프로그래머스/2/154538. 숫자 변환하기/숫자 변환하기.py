from collections import deque
def solution(x, y, n):
    visit = set()
    depth = 0
    dd = deque()
    
    dd.append((x, depth))
    
    while dd:
        a, b = dd.popleft()

        if a == y:
            return b
        else:
            if a+n <= y and (a+n) not in visit:
                dd.append((a+n, b+1))
                visit.add(a+n)
            if a*2 <= y and (a*2) not in visit:
                dd.append((a*2, b+1))
                visit.add(a*2)
            if a*3 <= y and (a*3) not in visit:
                dd.append((a*3, b+1))
                visit.add(a*3)
    
    return -1

    