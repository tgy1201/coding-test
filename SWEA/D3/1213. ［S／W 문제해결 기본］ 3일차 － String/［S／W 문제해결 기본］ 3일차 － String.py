def compare(s):
    if s == K:
        return 1
    else:
        return 0

for i in range(10):
    N = int(input())

    K = input()
    S = input()

    cnt = 0
    for index, j in enumerate(S):
        if j == K[0] and index+len(K) <= len(S):
            cnt += compare(S[index:index+len(K)])
    print(f"#{i+1} {cnt}")
#shift+F10