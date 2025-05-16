a = int(input())

def convert(n):
    d = {"A": "1010", "B": "1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
    
    if n in d.keys():
        return d[n]
    else:
        a = bin(int(n))[2:]
        if len(a) != 4:
            a = "0"*(4-len(a)) + a
        return a
            
for i in range(a):
    l, num = map(str, input().split())
    answer = ''
    for j in num:
        answer += convert(j)
    print(f"#{i+1} {answer}")
        