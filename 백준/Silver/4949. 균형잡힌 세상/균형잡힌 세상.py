import sys
s = input()
cnt = 0
cnt2 = 0
arr = [] * len(s)
while s != ".":
    cnt = 0
    cnt2 = 0
    arr = [] * len(s)
    for x in range(0, len(s)):
        if cnt <= -1 or cnt2 <= -1:
            cnt = 5
            break
        if s[x] == "[":
            cnt = cnt + 1
            arr.append("[")
        elif s[x] == "]":
            cnt = cnt - 1
            if len(arr) >= 1:
                if arr[len(arr)-1] == "[":
                    arr.pop(len(arr)-1)

        if s[x] == "(":
            cnt2 = cnt2 + 1
            arr.append("(")
        elif s[x] == ")":
            cnt2 = cnt2 - 1
            if len(arr) >= 1:
                if arr[len(arr)-1]:
                    arr.pop(len(arr)-1)

        if s[x] == ".":
            break
    
    if cnt == 0 and cnt2 == 0 and len(arr) == 0:
        print("yes")
    else:
        print("no")
      
    s = input()
    