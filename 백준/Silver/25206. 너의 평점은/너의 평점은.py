cnt = 0
total = 0.0
arr = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for x in range(20):
    a, b, c = map(str, input().split())
    if c == "P":
        pass
    else:
        cnt = cnt + float(b)
        total = total + float(b)*arr[c]

print(total/cnt)
