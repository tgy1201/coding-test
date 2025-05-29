import sys
M = int(input())

S = set()
SS = set({str(j+1) for j in range(20)})

for i in range(M):
    T = list(map(str, sys.stdin.readline().split()))

    if T[0] == "add":
        S.add(T[1])
    elif T[0] == "check":
        if T[1] in S:
            print(1)
        else:
            print(0)
    elif T[0] == "remove":
        S.discard(T[1])
    elif T[0] == "toggle":
        if T[1] in S:
            S.remove(T[1])
        else:
            S.add(T[1])
    elif T[0] == "all":
        S = SS.copy()
    elif T[0] == "empty":
        S.clear()