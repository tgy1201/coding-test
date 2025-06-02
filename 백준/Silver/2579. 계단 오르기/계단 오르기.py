n = int(input())

li = []
for _ in range(n):
    x = int(input())
    li.append(x)

temp = [0]*(n+1)

if n == 1:
    print(li[0])
elif n == 2:
    print(li[0]+li[1])
elif n == 3:
    print(max(li[0]+li[2], li[1]+li[2]))
else:
    temp[0] = li[0]
    temp[1] = li[0]+li[1]
    temp[2] = max(li[0]+li[2], li[1]+li[2])

    for i in range(3, n):
        temp[i] = max(li[i]+temp[i-2], li[i]+li[i-1]+temp[i-3])

    print(temp[n-1])