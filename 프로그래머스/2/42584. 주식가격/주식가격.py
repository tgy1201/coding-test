def solution(prices):
    dd = [0] * len(prices)

    for i in range(0, len(prices)-1):
        for j in range(i+1, len(prices)):
            dd[i] += 1
            if prices[i] > prices[j]:
                break
    return dd