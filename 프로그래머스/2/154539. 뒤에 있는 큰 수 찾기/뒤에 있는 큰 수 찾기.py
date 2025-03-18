def solution(numbers):
    numbers.reverse()
    answer = []
    temp = []
    
    for i in numbers:
        while temp:
            if temp[-1] > i:
                answer.append(temp[-1])
                temp.append(i)
                break
            temp.pop()
        
        if len(temp) == 0:
            answer.append(-1)
            temp.append(i)
            continue
    answer.reverse()
    return answer
'''
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        check = 0
        for j in range(i, len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                check = 1
                break
        if check == 0:
            answer.append(-1)
    answer.append(-1)
    
    return answer
'''