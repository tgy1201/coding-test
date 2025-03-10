import heapq
def solution(N, road, K):
    answer = 0
    
    dd = {}
    
    for i in range(N):
        dd[i+1] = []
        
    for i in road:
        dd[i[0]].append((i[1],i[2]))
        dd[i[1]].append((i[0],i[2]))
    
    def cal(start):
        distances = {node: 500001 for node in dd.keys()}
        distances[start] = 0
        
        pq = [(0, start)]
        
        while pq:
            distance, node = heapq.heappop(pq)
            
            if distance > distances[node]:
                continue
            
            for nn, nd in dd[node]:
                if distances[nn] > distance + nd:
                    distances[nn] = distance + nd
                    heapq.heappush(pq, (distance + nd, nn))
        return distances
    return len([i for x in cal(1).keys() if cal(1)[x] <= K])
    
    
        

'''
def solution(N, road, K):
    answer = 0
    
    dd = {}
    
    for i in range(N):
        dd[i+1] = []
        
    for i in road:
        dd[i[0]].append([i[1],i[2]])
        dd[i[1]].append([i[0],i[2]])
    s = set(dfs(1, K, dd, [1], 0))
    return len(s) + 1

def dfs(n, k, dd, arr, dep):
    d = []
    for i in dd[n]:
        if i[0] in arr:
            continue
        if dep + i[1] > k:
            continue
        arr.append(i[0])
        d.append(i[0])
        d.extend(dfs(i[0], k, dd, arr, dep + i[1]))
        arr.remove(i[0])
    return d
'''
