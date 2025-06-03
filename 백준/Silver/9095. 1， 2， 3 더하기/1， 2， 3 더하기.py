T = int(input())

c = [set() for _ in range(12)]

c[1] = set(("1"))
c[2] = set(("1+1","2"))
c[3] = set(("1+1+1","1+2","2+1","3"))

for i in range(4, 12):
    for j in range(1, i):
        for k in c[j]:
            for l in c[i-j]:
                c[i].add(f"{k}+{l}")

for _ in range(T):
    s = int(input())

    print(len(c[s]))