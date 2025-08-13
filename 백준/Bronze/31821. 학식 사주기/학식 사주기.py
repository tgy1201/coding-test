import sys

input = sys.stdin.readline

menu = []

n = int(input())

for i in range(n):
    menu.append(int(input()))

m = int(input())
s = 0

for i in range(m):
    s += menu[int(input())-1]

print(s)
