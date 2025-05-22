from collections import deque
for i in range(10):
    T = int(input())

    li = deque(map(int, input().split()))

    cnt = 1
    while True:
        f = li.popleft()

        if cnt % 5 == 0:
            cnt = 5
        else:
            cnt = cnt % 5
        if f - cnt > 0:
            li.append(f-cnt)
        else:
            li.append(0)
            break
        cnt += 1
    print(f"#{i+1} {' '.join(map(lambda x: str(x), li)) }")


#shift+F10