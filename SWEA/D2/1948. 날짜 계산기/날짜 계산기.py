import math
T = int(input())

for i in range(T):
    dic = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    li = list(map(int, input().split()))
    
    a = sum(dic[:li[0]]) + li[1]
    b = sum(dic[:li[2]]) + li[3]
    
    print(f"#{i+1} {b-a+1}")