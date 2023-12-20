n, x = map(int, input().split())

A = map(int, input().split())
str = ""
for i in A:
    if i < x:
        str += f"{i} "
    else:
        pass

print(str)