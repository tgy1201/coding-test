import sys
input = sys.stdin.readline

interval = (int(input())-1)*7

year = 2024
month = 8 + interval

year += month // 12
month = month % 12

if month == 0:
    print(f"{year-1} 12")
else:
    print(f"{year} {month}")