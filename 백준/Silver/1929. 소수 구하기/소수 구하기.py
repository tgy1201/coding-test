n, m = map(int, input().split())
cnt = 0

for x in range(n, m+1):
    cnt = 0
    if x == 1:
        cnt = 1
    for y in range(2, int(x**0.5)+1):
         if x % y == 0:
             cnt = 1
             break   
    if cnt == 0:
        print(x)