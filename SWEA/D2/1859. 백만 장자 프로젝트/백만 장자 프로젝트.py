T = int(input())

for i in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    
    temp = []
    profit = 0
    for j in li:
        if len(temp) == 0:
            temp.append(j)
            continue
 
        for k in range(len(temp)-1, -1, -1):
            if temp[k] < j:
                profit += j-temp[k]
                temp[k] = j
            else:
                break
        temp.append(j)
    print(f"#{i+1} {profit}")