from collections import Counter
T = int(input())

for i in range(T):
    N, M, K = map(int, input().split())

    answer = "Possible"
    s = list(map(int, input().split()))
    dd = dict(Counter(s))
    s = list(set(s))
    s.sort()

    cnt = 0
    index = 0
    for j in range(1, s[-1]+1):
        if j % M == 0:
            cnt += K
        if j == s[index]:
            if cnt - dd[s[index]] < 0:
                answer = "Impossible"
                break
            else:
                cnt -= dd[s[index]]
                index += 1
                
    if s.count(0) != 0:
        print(f"#{i+1} Impossible")
    else:
        print(f"#{i+1} {answer}")