x, y, w, h = map(int, input().split())
a = 0
b = 0

if x >= ( w / 2):
    a = w - x
else:
    a = x

if y >= ( h / 2):
    b = h - y
else:
    b = y

if a > b:
    print(b)
else:
    print(a)