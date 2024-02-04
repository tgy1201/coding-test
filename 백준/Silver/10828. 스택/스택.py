import sys

n = int(sys.stdin.readline())
arr = [] * n
for x in range(n):
    s = sys.stdin.readline()
    if "push" in s:
        a =s.split()
        arr.append(a[1])
    elif "pop" in s:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
            arr.pop()
    elif "size" in s:
        print(len(arr))
    elif "empty" in s:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif "top" in s:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])


