T = int(input())

for i in range(T):
    li = list(map(int, input().split()))
    
    li.remove(max(li))
    li.remove(min(li))
    
    print(f"#{i+1} {round(sum(li)/8)}")