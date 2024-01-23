a, b = map(int, input().split())
count = 0
for x in range(1, a+1):
    if a%x == 0:
        count = count + 1
    if count == b:
        print(x)
        break
if count < b:
    print(0)