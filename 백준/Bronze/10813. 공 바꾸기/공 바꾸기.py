n,m = map(int, input().split())
arr = [0] * n
str = ""
for a in range(1, n+1):
    arr[a-1]=a

for b in range(1, m+1):
    i,j = map(int, input().split())
    buffer = arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=buffer

for c in range(1, n+1):
    str += f"{arr[c-1]} "

print(str)