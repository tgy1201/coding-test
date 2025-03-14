def solution(number, k):
    stack = []  # 결과를 저장할 스택
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 이전 숫자를 제거 (k개 제거할 때까지)
            k -= 1
        stack.append(num)  # 현재 숫자 추가
    
    # 남은 k개를 제거해야 하면, 뒤에서 자르기
    return ''.join(stack[:len(number) - k])

'''
import copy
def solution(number, k):
    aa = copy.deepcopy(number)
    k = len(number) - k
    number = [[x, -index] for index, x in enumerate(number)]
    answer = {}
    a = ''

    cnt = 0
    while k != cnt:
        m = number.index(max(number))

        answer[-max(number)[1]] = 0
        if len(number[m:]) + cnt == k:
            break
        elif len(number[m:]) + cnt < k:
            cnt += len(number[m:])
            answer[-max(number)[1]] = len(number[m:]) -1
            number = number[:m]
        else:
            cnt += 1
            number = number[m+1:]
    
    for i in sorted(answer.keys()):
        c = answer[i]
        a += aa[i:i+c+1]
    return a
'''