k, n = map(int, input().split())
str = [] * k
cnt = 0

for x in range(k):
    l = int(input())
    cnt = cnt + l
    str.append(l)
str = sorted(str)

end = cnt // n + 1
start = 0
mid = (end + start) // 2
check = -1
while end - start != 1:
    a = 0
    for x in range(0, len(str)):
        a = a + str[x]//mid
    if a < n:
        end = mid
        mid = (end+start) // 2
        check = 1
    elif a >= n:
        start = mid
        mid = (end+start) // 2
        check = 0
b = 0

for x in range(0, len(str)):
    b = b + str[x]// end
if b >=n:
    print(end)
else:
    print(mid)



