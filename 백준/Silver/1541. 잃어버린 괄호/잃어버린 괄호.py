import sys

s = sys.stdin.readline().strip()

num = []
op = []
temp = ''
for i in s:
    if i.isdigit():
        temp += i
    else:
        op.append(i)
        num.append(int(temp))
        temp = ''
num.append(int(temp))

answer = [num[0]]
for i in range(len(op)):
    if op[i] == "+":
        answer[-1] += num[i+1]
    else:
        answer.append(num[i+1])

a = answer[0]

if len(answer) == 1:
    print(a)
else:
    for i in range(1, len(answer)):
        a -= answer[i]
    print(a)