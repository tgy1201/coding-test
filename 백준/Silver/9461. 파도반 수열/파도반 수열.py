T = int(input())

temp = [1,1,1,2,2,3,4,5,7,9]

for i in range(11,101):
    sum = temp[-1] + temp[-5]
    temp.append(sum)

for i in range(T):
    n = int(input())

    print(temp[n-1])