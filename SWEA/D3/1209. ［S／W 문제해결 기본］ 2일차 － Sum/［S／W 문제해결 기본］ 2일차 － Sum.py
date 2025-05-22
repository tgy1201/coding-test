for i in range(10):
    T = int(input())
    li = []
    a = 0
    b = 0
    for j in range(100):
        e = list(map(int, input().split()))
        if len(li) == j:
            a += e[j]
            b += e[99-j]
        li.append(e)

    ll = [[0]*100 for _ in range(100)]

    for j in range(100):
        for k in range(100):
            ll[j][k] = li[k][j]

    c = []
    d = []
    for j in range(100):
        c.append(sum(li[j]))
        d.append(sum(ll[j]))

    answer = max(a, b, max(c), max(d))

    print(f"#{i+1} {answer}")

#shift+F10