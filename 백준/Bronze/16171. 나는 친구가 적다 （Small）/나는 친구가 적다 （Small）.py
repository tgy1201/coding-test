import sys
input = sys.stdin.readline

S = input().strip()
K = input().strip()

dq = []
check = 0
for i in S:
    if not i.isdigit():
        dq.append(i)

        if len(dq) >= len(K) and ''.join(dq[-len(K):]) == K:
            check = 1
            break
    if check == 1:
        break

if check == 1:
    print(1)
else:
    print(0)