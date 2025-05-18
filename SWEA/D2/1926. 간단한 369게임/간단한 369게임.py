N = int(input())

answer = ""
dic = ["3", "6", "9"]
for i in range(N):
    e = str(i+1)
    cnt = 0
    for j in e:
        if j in dic:
            cnt += 1
    if cnt != 0:
        e = "-"*cnt
    answer += e + " "
    
print(answer)