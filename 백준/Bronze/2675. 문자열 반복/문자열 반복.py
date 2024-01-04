s = int(input())

for i in range(s):
    r, p = map(str, input().split())
    st = ""
    for j in range(len(p)):
        st += p[j]*int(r)
    print(st)