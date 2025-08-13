import sys

input = sys.stdin.readline

n = int(input())

m = input()
li = []
for i in m:
    li.append(i)

for i in range(n-1):
    s = input()

    for j in range(len(li)):
        if li[j] == "?":
            continue

        if s[j] != li[j]:
            li[j] = "?"

print(''.join(li))