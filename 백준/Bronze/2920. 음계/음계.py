arr = list(map(int, input().split()))
cnt = 0
for x in range(1, 9):
    if x == arr[x-1]:
        cnt = cnt + 1
    if x == arr[8-x]:
        cnt = cnt - 1

if cnt == 8:
    print("ascending")
elif cnt == -8:
    print("descending")
else:
    print("mixed")