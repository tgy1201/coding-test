import math
def solution(n, k):
    p = [i+1 for i in range(n)]
    
    answer = []
    for i in range(n, 1, -1):
        s = fact(i-1)
        r = math.ceil(k/s)
        k = k % s

        answer.append(p[r-1])
        p.remove(p[r-1])
    answer.append(p[-1])
    return answer
def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)
'''
from itertools import permutations
def solution(n, k):
    answer = []
    p = [i+1 for i in range(n)]
    
    return list(permutations(p))[k-1]
'''