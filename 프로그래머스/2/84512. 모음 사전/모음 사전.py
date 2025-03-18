from itertools import product

def solution(word):
    lis = list()
    words = ['A','E','I','O','U']
    for j in range(1,6):
        for i in product(words,repeat=j):
            lis.append(list(i))
    lis.sort()
    
    cnt = 0
    for i in lis:
        s = ''.join(i)
        cnt += 1
        
        if word == s:
            return cnt