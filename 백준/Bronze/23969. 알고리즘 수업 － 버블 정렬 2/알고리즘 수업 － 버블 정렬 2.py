import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

for _ in range(n):
    for i in range(n-1):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            cnt += 1
            if cnt == k:
                print(' '.join(map(str, li)))
                exit()
print(-1)