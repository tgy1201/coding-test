from collections import deque

def solution(cacheSize, cities):
    answer = 0
    a = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in cities:
        i = i.lower()
        if len(a) < cacheSize:
            if i in a:
                answer += 1
                a.remove(i)
                a.append(i)
            else:
                a.append(i)
                answer += 5
        else:
            if i in a:
                answer +=1
                a.remove(i)
                a.append(i)
            else:
                a.popleft()
                a.append(i)
                answer +=5
            
    return answer