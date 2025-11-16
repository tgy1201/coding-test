import sys
input = sys.stdin.readline

a, b = map(str, input().strip().split())

def fiveToSix(s, reverse):
    if reverse:
        return int(s.replace("5", "6"))

    return int(s.replace("6", "5"))

mi = fiveToSix(a, False) + fiveToSix(b, False)
ma = fiveToSix(a, True) + fiveToSix(b, True)

print(f"{mi} {ma}")