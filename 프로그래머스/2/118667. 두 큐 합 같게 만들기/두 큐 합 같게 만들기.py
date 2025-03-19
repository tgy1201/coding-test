from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    a, b = sum(queue1), sum(queue2)

    cnt = 0
    end = len(queue1)
    while cnt <= end * 3:
        if a == b:
            return cnt
        elif a < b:
            x = queue2.popleft()
            b -= x
            a += x
            queue1.append(x)
        else:
            y = queue1.popleft()
            a -= y
            b += y
            queue2.append(y)
        cnt += 1
    return -1