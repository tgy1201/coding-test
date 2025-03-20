from collections import defaultdict
def solution(n, wires):
    dd = defaultdict(list)
    answer = []
    
    for x, y in wires:
        dd[x].append(y)
        dd[y].append(x)
        
    def dfs(a, b, visit, cnt):
        visit.add(a)
        cnt = 1
        
        for i in dd[a]:
            if i not in visit and i != b:
                cnt += dfs(i, b, visit, cnt)
        return cnt
    
    for x, y in wires:
        visit = set()
        left = dfs(x, y, visit, 0)
        right = dfs(y, x, visit, 0)
        answer.append(abs(left-right))
        
    return min(answer)