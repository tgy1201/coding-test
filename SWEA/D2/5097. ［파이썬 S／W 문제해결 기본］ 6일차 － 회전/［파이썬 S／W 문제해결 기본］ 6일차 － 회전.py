from collections import deque
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    li = deque(map(int, input().split()))
    
    for j in range(M):
        s = li.popleft()
        li.append(s)
    print(f"#{i+1} {li.popleft()}")