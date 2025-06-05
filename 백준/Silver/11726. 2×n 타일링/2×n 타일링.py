N = int(input())

temp = [0] * 1001
temp[0] = 1
temp[1] = 2
for i in range(2, 1001):
    temp[i] = temp[i-1] + temp[i-2]

print(temp[N-1]%10007)