from itertools import combinations
import copy
def solution(relation):
    dd = {i: [] for i in range(len(relation[0]))}
    cnt = 0
    test = []
    
    for i in relation:
        for index, j in enumerate(i):
            dd[index].append(j)
    
    length = len(dd)
    for i in range(1, length+1):
        com = combinations(dd.keys(), i)
        check = []
        for j in com:
            tup = [dd[k] for k in j]
            row = zip(zip(*tup))
            a = copy.deepcopy(row)

            if sorted(list(a)) == sorted(list(set(row))):
                test.append(j)
                cnt += 1
                check.extend(j)
                continue
    sets = [set(sublist) for sublist in test]  # 리스트를 집합으로 변환
    result = []

    for s in sets:
        if not any(s > other for other in sets):  # 다른 집합을 포함하는 경우 제외
            result.append(list(s))  # 원래 리스트 형태로 변환해서 저장
    
    return len(result)
    
    return result