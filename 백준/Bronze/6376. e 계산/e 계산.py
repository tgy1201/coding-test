import sys, math
input = sys.stdin.readline

print("n e")
print("- -----------")
print("0 1")
print("1 2")
print("2 2.5")
e = 2.5
for i in range(3, 10):
    e += 1 / math.factorial(i)
    print("{:d} {:.9f}".format(i, e))