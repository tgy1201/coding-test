T = int(input())

for i in range(T):
    H, W = map(int, input().split())

    user = ["<", ">", "^", "v"]
    x, y = 0, 0
    li = []
    for j in range(H):
        e = input()

        ll = []
        for index, k in enumerate(e):
            if k in user:
                x, y = index, j
            ll.append(k)
        li.append(ll)

    N = int(input())
    com = input()

    for j in com:
        if j == "U":
            li[y][x] = "^"

            if y-1 >= 0 and li[y-1][x] == ".":
                li[y-1][x], li[y][x] = li[y][x], li[y-1][x]
                y -= 1
        elif j == "D":
            li[y][x] = "v"

            if y+1 < len(li) and li[y+1][x] == ".":
                li[y+1][x], li[y][x] = li[y][x], li[y+1][x]
                y += 1
        elif j == "L":
            li[y][x] = "<"

            if x-1 >= 0 and li[y][x-1] == ".":
                li[y][x-1], li[y][x] = li[y][x], li[y][x-1]
                x -= 1
        elif j == "R":
            li[y][x] = ">"

            if x + 1 < len(li[0]) and li[y][x + 1] == ".":
                li[y][x + 1], li[y][x] = li[y][x], li[y][x + 1]
                x += 1
        else:
            if li[y][x] == "^":
                temp = y

                while temp-1 >= 0:
                    if li[temp-1][x] == "*":
                        li[temp-1][x] = "."
                        break
                    elif li[temp-1][x] == "#":
                        break
                    temp -= 1
            elif li[y][x] == "v":
                temp = y

                while temp+1 < len(li):
                    if li[temp + 1][x] == "*":
                        li[temp + 1][x] = "."
                        break
                    elif li[temp + 1][x] == "#":
                        break
                    temp += 1
            elif li[y][x] == "<":
                temp = x

                while temp-1 >= 0:
                    if li[y][temp-1] == "*":
                        li[y][temp-1] = "."
                        break
                    elif li[y][temp-1] == "#":
                        break
                    temp -= 1
            elif li[y][x] == ">":
                temp = x

                while temp+1 < len(li[0]):
                    if li[y][temp + 1] == "*":
                        li[y][temp + 1] = "."
                        break
                    elif li[y][temp + 1] == "#":
                        break
                    temp += 1
    print(f"#{i+1}", end=" ")

    for j in li:
        print(''.join(j))