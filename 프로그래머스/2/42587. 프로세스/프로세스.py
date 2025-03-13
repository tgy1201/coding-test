from collections import deque

def solution(priorities, location):
    priorities = [[x, i] for i, x in enumerate(priorities)]
    cnt = 0
    #return list(priorities)

    while priorities:
        m = max(priorities)
        
        idx = 0
        for index, i in enumerate(priorities):
            if m[0] == i[0]:
                idx = index
                break
                
        for _ in range(idx):
            priorities.append(priorities.pop(0))
        print(priorities)
        a = priorities.pop(0)
        cnt += 1

        if a[1] == location:
            return cnt
        