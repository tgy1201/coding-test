from collections import defaultdict

T = int(input())


for i in range(T):
    s = int(input())
    dd = defaultdict(int)

    for _ in range(s):
        a, b = map(str, input().split())
        dd[b] += 1

    cnt = 1
    for j in dd.keys():
        cnt *= dd[j]+1

    print(cnt-1)