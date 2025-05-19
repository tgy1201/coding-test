T = int(input())

for i in range(T):
    S = input()
    
    temp = []
    index = 0
    s = S[index]
    cnt = 1
    for j in range(1, len(S)):
        if S[j] != s:
            cnt += 1
        else:
            temp.append(cnt)
            index += 1
            s = S[index]
    temp.append(cnt)
    print(f"#{i+1} {max(temp)}")
         