from itertools import permutations
def solution(numbers):
    dd = [i for i in numbers]
    total = []
    for i in range(1, len(numbers)+1):
        a = permutations(dd, i)
        b = [''.join(x) for x in a]
        total.extend(b)
    total = set([int(x) for x in total])
    
    cnt = 0
    for i in total:
        if(cal(i)):
            cnt +=1
    return cnt

def cal(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True