import sys
input = sys.stdin.readline

li = list(map(int, input().split()))

for j in range(5):
    for i in range(4):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            answer = ' '.join(map(str, li))
            print(answer)

            if answer == '1 2 3 4 5':
                exit()