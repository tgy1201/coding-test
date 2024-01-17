a = int(input())

for b in range(1, a+1):
    print(" "*(a-b)+"*"*b+"*"*(b-1))

for c in range(a-1, 0, -1):
    print(" "*(a-c)+"*"*c+"*"*(c-1))