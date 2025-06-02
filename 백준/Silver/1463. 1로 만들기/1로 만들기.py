from collections import deque
N = int(input())
dq = deque()
dq.append((1,0))
visit = set()
visit.add(1)

cnt = 0
while dq:
    x, depth = dq.popleft()

    if x == N:
        print(depth)
        break
        
    for next_x in [x * 3, x * 2, x + 1]:
        if next_x <= N and next_x not in visit:
            visit.add(next_x)
            dq.append((next_x, depth + 1))