n = int(input())

arr = map(int, input().split())

v = int(input())

count = 0
for i in arr:
    if i == v:
        count+= 1
    else:
        pass

print(count)