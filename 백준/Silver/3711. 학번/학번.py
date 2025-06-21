import sys
input = sys.stdin.readline

N= int(input())

for _ in range(N):
    G = int(input())

    s = set()
    for i in range(G):
        student = int(input())

        s.add(student)

    cnt = 1
    while True:
        ss = set()
        for i in s:
            ss.add(pow(i, 1, cnt))

        if len(ss) == G:
            print(cnt)
            break
        cnt += 1
