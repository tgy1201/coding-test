from collections import Counter
T = int(input())

for i in range(T):
    N = int(input())
    
    li = list(map(int, input().split()))
    
    a = Counter(li).most_common()
    
    answer = sorted(a, key= lambda x: (x[1],x[0]), reverse=True)
    
    print(f"#{N} {answer[0][0]}")