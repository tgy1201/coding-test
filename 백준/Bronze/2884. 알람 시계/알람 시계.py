H, M = map(int,input().split())


if H>0 or (H==0 and M>=45):
    MM = H*60 + M - 45
    A = MM//60
    B = int(MM%60)
else:
    MM = 1440 + M - 45
    A = MM//60
    B = int(MM%60)

print(f"{A} {B}")