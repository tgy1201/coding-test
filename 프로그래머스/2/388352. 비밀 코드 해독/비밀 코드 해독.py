from itertools import combinations
def solution(n, q, ans):
    d = [x+1 for x in range(n)]
    a = list(combinations(d, 5))
    answer = 0
    cnt = 0
    
    for i in a:
        check = 0
        for index, j in enumerate(q):
            cnt = 0
            for k in j:
                if(k in i):
                    cnt +=1
                else:
                    continue
            if ans[index] != cnt:
                check = 1
                break
        if(check == 0):
            answer +=1

    return answer