import sys, math

input = sys.stdin.readline

M = int(input())
answer = 0

for _ in range(M):
    S, N = map(int, input().split())

    gcd = math.gcd(N,S)
    a = N // gcd
    b = S // gcd
    bb = pow(b, 1000000005, 1000000007)
    c = (a * bb) % 1000000007
    answer += c

print(answer%1000000007)