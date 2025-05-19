T = int(input())

for i in range(T):
    S = input()
    
    r = ''
    l = ''
    if len(S) % 2 == 0:
        r = S[:len(S)//2]
        l = S[len(S)//2:]
    else:
        r = S[:len(S)//2]
        l = S[len(S)//2+1:]
    l = l[::-1]

    if r == l:
        print(f"#{i+1} {1}")
    else:
        print(f"#{i+1} {0}")