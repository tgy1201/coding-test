arr = [1, 1, 2, 2, 2, 8]
str = ""

a = map(int, input().split())
count = 0

for x in a:
    b = arr[count] - x
    count = count + 1
    str += f"{b} "

print(str)