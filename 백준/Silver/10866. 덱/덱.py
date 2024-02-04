import sys
import collections
n = int(sys.stdin.readline())

arr = collections.deque()

for x in range(n):
    s = sys.stdin.readline()
    if "push_front" in s:
        a =s.split()
        arr.appendleft(a[1])
    elif "push_back" in s:
        a =s.split()
        arr.append(a[1])
    elif "pop_front" in s:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
            arr.popleft()
    elif "pop_back" in s:
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
    elif "front" in s:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif "back" in s:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])


