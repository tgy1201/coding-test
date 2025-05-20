T = int(input())

for i in range(T):
    B = input()
    
    li = []
    for j in B:
        if len(li) == 0 and j == "0":
            continue
        
        if j == "1":
            if len(li) == 0 or li[-1] == "0":
                li.append("1")
        else:
            if li[-1] == "1":
                li.append("0")
    print(f"#{i+1} {len(li)}")