from collections import Counter
T = int(input())

for i in range(T):
    s = input()
    answer = []
    dd = Counter(s)

    for j in dd.keys():
        if dd[j] % 2 != 0:
            answer.append(j)

    answer.sort()

    if len(answer) == 0:
        print(f"#{i+1} Good")
    else:
        print(f"#{i+1} {''.join(answer)}")


#shift+F10