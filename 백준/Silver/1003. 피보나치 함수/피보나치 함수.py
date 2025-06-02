T = int(input())

aa = [[0]*2 for _ in range(41)]
aa[0] = [1,0]
aa[1] = [0,1]

for i in range(2, 41):
    aa[i] = [aa[i-1][0]+aa[i-2][0], aa[i-1][1]+aa[i-2][1]]

for i in range(T):
    n = int(input())

    print(f"{aa[n][0]} {aa[n][1]}")