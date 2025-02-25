def solution(wallet, bill):
    answer = 0
    
    while(1):
        if(max(wallet) < max(bill) or min(wallet) < min(bill)):
            if(bill[0] > bill[1]):
                bill[0] //= 2
            else:
                bill[1] //= 2
            answer +=1
        else:
            break
    return answer