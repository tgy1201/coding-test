A = int(input())
B = int(input())

E = A*(B//100)
F = A*B
D = F-10*A*(B//10)
C = F-100*E-D

print(D)
print(C//10)
print(E)
print(F)
