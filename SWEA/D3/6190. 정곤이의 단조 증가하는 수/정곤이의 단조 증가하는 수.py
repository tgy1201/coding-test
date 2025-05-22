def calc(s):
    for i in range(0, len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True

T = int(input())

for i in range(T):
    N = int(input())

    A = list(map(int, input().split()))

    li = set()
    for j in range(len(A)):
        for k in range(j+1, len(A)):
            if calc(str(A[j]*A[k])):
                li.add(A[j]*A[k])
    if len(li) == 0:
        print(f"#{i+1} -1")
    else:
        print(f"#{i+1} {max(li)}")
#shift+F10