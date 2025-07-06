import sys

input = sys.stdin.readline

N = int(input())

S = input().strip()

if S[0] == "B" or S[-1] == "A":
    print("No")
else:
    print("Yes")