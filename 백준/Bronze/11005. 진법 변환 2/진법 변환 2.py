a, b = map(int,input().split())
str = ""
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while a:
    str += f"{arr[a%b]}"
    a //= b

print(str[::-1])