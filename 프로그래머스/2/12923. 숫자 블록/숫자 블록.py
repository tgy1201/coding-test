def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        if i == 2 or i ==3:
            answer.append(1)
            continue
        p = [1]
        for j in range(2, int(i**0.5)+1):
            if(i%j == 0):
                if(i//j == j):
                    p.append(j)
                elif(i//j <= 10**7):
                    p.extend([j, i//j])
                elif(i//j > 10**7):
                    p.append(j)
        answer.append(max(p))
    return answer

'''

'''