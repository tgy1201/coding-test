import math
def solution(arr):
    answer = 0
    a = arr[0]
    
    for i in range(1, len(arr)):
        a = (a*arr[i]) // math.gcd(arr[i], a)
    return a