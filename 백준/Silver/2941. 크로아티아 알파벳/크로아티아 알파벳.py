arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
a = input()
cnt = len(a)

for b in arr:
    if b in a:
        cnt = cnt - a.count(b)

print(cnt)