for i in range(10):
    N = int(input())

    li = []

    for j in range(100):
        e = input()
        ll = []
        for k in e:
            ll.append(k)
        li.append(ll)

    cp = [["0"]*100 for _ in range(100)]
    for j in range(100):
        for k in range(100):
            cp[j][k] = li[k][j]

    answer = -1

    for j in range(100):
        for k in range(100):
            if k % 2 == 0:
                a = 1
                while k + 2 * a <= 100:
                    if li[j][k:k + a] == li[j][k + (2 * a) - 1:k + a - 1:-1]:
                        answer = max(answer, 2 * a)
                    if cp[j][k:k + a] == cp[j][k + (2 * a) - 1:k + a - 1:-1]:
                        answer = max(answer, 2 * a)
                    a += 1

                b = 1
                while k + 2 * b + 1 <= 99:
                    if li[j][k:k + b] == li[j][k + 2 * b:k + b:-1]:
                        answer = max(answer, 2 * b + 1)
                    if cp[j][k:k + b] == cp[j][k + 2 * b:k + b:-1]:
                        answer = max(answer, 2 * b + 1)
                    b += 1
            else:
                a = 1
                while k + 2 * a <= 99:
                    if li[j][k:k + a] == li[j][k + (2 * a) - 1:k + a - 1:-1]:
                        answer = max(answer, 2 * a)
                    if cp[j][k:k + a] == cp[j][k + (2 * a) - 1:k + a - 1:-1]:
                        answer = max(answer, 2 * a)
                    a += 1

                b = 1
                while k + 2 * b + 1 <= 100:
                    if li[j][k:k + b] == li[j][k + 2 * b:k + b:-1]:
                        answer = max(answer, 2 * b + 1)
                    if cp[j][k:k + b] == cp[j][k + 2 * b:k + b:-1]:
                        answer = max(answer, 2 * b + 1)
                    b += 1

    print(f"#{N} {answer}")
#shift+F10