A, B = map(int,input().split())
C = int(input())
time = A*60 + B + C
hour = time//60
min = time%60

if hour>=24:
    print(f"{hour-24} {min}")
else:
    print(f"{hour} {min}")