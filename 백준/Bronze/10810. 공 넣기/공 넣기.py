n,m = map(int, input().split())
arr = [0] * n
str = ""
for a in range(1, m+1):
    i,j,k = map(int, input().split())
    for b in range(i, j+1):
        arr[b-1] = k

for c in range(1, n+1):
    str += f"{arr[c-1]} "

print(str)