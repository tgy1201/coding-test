a, b, c = map(int, input().split())

if a+b<=c:
    c = a+b-1
elif a+c<=b:
    b = a+c-1
elif b+c<=a:
    a = b+c-1
print(a+b+c)