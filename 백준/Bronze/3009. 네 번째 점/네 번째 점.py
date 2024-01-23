a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g = 0
h = 0
if a == c:
    g = e
elif a == e:
    g = c
else:
    g = a

if b == d:
    h = f
elif b == f:
    h = d
else:
    h = b
print(f"{g} {h}") 
