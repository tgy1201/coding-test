def solution(n):
    num = int(n**0.5)
    if(num ** 2 == n):
        answer = (num + 1) ** 2
    else:
        answer = -1
    return answer