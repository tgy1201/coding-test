import sys, copy

input = sys.stdin.readline

total = 0
for i in range(4):
    s = int(input())
    total += s

print(total//60)
print(total%60)
