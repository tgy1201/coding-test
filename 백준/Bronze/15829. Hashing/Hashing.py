import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
cnt = 0
m = 1234567891
for x in range(0, n):
    cnt += (ord(s[x])-96) * (31**x)
print(cnt % m)