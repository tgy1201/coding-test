from collections import defaultdict
T = int(input())

for i in range(T):
    N = int(input())
    dd = defaultdict(int)

    for j in range(N):
        A, B = map(int, input().split())

        for k in range(A, B+1):
            dd[k] += 1
    P = int(input())

    answer = ''
    for _ in range(P):
        C = int(input())
        answer += str(dd[C]) + " "

    print(f"#{i+1} {answer}")

#shift+F10