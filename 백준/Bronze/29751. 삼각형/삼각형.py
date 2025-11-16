import sys
input = sys.stdin.readline

w, h = map(int, input().split())

answer = w * h * 0.5

print('{0:0.1f}'.format(answer))