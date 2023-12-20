n = int(input())

A = map(int, input().split())

min = 1000001
max = -1000001
for i in A:
    if min > i:
        min = i
    else:
        pass

    if max < i:
        max = i
    else:
        pass

print(f"{min} {max}")