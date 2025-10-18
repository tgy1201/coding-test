import sys
input = sys.stdin.readline

N, W, H, L = map(int, input().split())

ww = W // L
hh = H // L

answer = min(N, ww*hh)

print(answer)