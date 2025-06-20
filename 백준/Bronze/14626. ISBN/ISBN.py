import sys
input = sys.stdin.readline

N = input().strip()
num = 0

x = 1
for index, i in enumerate(N):
    if index == len(N)-1:
        m = int(i)
        break
    if i.isdigit():
        if index % 2 ==0:
            num += int(i)
        else:
            num += int(i) *3
    else:
        if index % 2 !=0:
            x = 3

for i in range(10):
    temp = 10 - (num+(i*x)) %10
    if m == 0 and temp == 10:
        print(i)
    elif m == temp:
        print(i)