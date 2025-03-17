from itertools import permutations
import copy
def solution(expression):
    op = []
    num = []
    s = ""
    for i in expression:
        if i == "+" or i =="-" or i == "*":
            num.append(int(s))
            s = ""
            op.append(i)
        else:
            s += i
    num.append(int(s)) # 마지막 숫자
    
    opp = list(permutations(set(op), len(set(op))))
    
    mm = -1
    for i in opp:
        cnum = copy.deepcopy(num)
        cop = copy.deepcopy(op)

        for j in i:
            temp = [cnum[0]]
            
            for index, k in enumerate(cop):
                if j == k and k == "+":
                    temp[-1] += cnum[index+1]
                elif j == k and k == "*":
                    temp[-1] *= cnum[index+1]
                elif j == k and k == "-":
                    temp[-1] -= cnum[index+1]
                else:
                    temp.append(cnum[index+1])
            cnum = copy.deepcopy(temp)
            cop = [x for x in cop if x != j]
        if abs(cnum[0]) > mm:
            mm = abs(cnum[0])
            
    return mm
                