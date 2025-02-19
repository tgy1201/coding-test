def solution(price, money, count):

    l = [x*price for x in range(1, count+1)]
    answer = sum(l) - money
    if(answer <= 0):
        return 0
    return answer