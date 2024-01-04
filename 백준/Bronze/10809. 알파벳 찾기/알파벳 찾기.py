s = input()
arr = [-1]*26
str2 =""

for i in range(97,123):
    for j in range(len(s)):
        if s[j] == chr(i) and arr[i-97] == -1:
            arr[i-97] = j

for k in arr:
    str2 += f"{k} "

print(str2)