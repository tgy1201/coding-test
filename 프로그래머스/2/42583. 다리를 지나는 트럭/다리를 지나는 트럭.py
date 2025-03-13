from collections import deque
def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)
    cnt = 0
    total = 0
    temp = deque()
    f = []

    while truck_weights != f:
        cnt += 1
        if wait and total + wait[0] <= weight:
            a = wait.popleft()
            temp.append(a)
            total += a
        else:
            temp.append(0)
        
        if cnt >= bridge_length:
            if temp and temp[0] != 0:
                b = temp.popleft()
                f.append(b)
                total -= b
            elif temp:
                temp.popleft()
    return cnt + 1
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)
    cnt = 0
    total = 0
    dd = deque()
    w = deque()
    f = []

    while truck_weights != f:
        if wait and total + wait[0] <= weight:
            total += wait[0]
            dd.append(wait.popleft())
            w.append(bridge_length)
        
        for i in range(len(w)):
            w[i] -= 1
            if dd and w[i] == 0:
                a = dd.popleft()
                f.append(a)
                total -= a
        
        cnt += 1
    return cnt + 1
'''