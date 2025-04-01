import math 
def solution(n, m):
    answer = []
    return list([math.gcd(n,m), (n*m)/math.gcd(n,m)])