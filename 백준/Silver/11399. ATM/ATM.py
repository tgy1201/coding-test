N = int(input())

K = list(map(int, input().split()))

K.sort()

temp = 0
answer = 0
for i in K:
    temp = temp+i
    answer = answer+temp
print(answer)