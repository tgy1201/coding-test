from collections import deque
def solution(sequence, k):
    total = deque()
    ss = 0
    a = 1000001
    b = 1000001
    
    for index, v in enumerate(sequence[::-1]):
        total.append(v)
        ss += v
        if ss == k:
            if a >= len(total) - 1 and b >= len(sequence)-index-1:
                a = len(total) - 1
                b = len(sequence)-index-1
            ss -= total[0]
            total.popleft()
        elif ss > k:
            ss -= total[0]
            total.popleft()
        else:
            continue
    return b, a+b