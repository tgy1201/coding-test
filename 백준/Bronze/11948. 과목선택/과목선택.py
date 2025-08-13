import sys

input = sys.stdin.readline

answer = 0
s = []

for i in range(4):
    s.append(int(input()))

answer = sum(s) - min(s)
s = []
for i in range(2):
    s.append(int(input()))

answer += sum(s) - min(s)

print(answer)