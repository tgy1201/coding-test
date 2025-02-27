from collections import Counter
def solution(n):
    nn = bin(n)[2:].count("1")
    while 1:
        n += 1
        a = bin(n)[2:].count("1")
        
        if(a == nn):
            return int(n)