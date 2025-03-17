from collections import Counter
import heapq

def solution(k, tangerine):
    tangerine = Counter(tangerine)
    cnt = 0
    answer = 0
    pq = []
    for i in tangerine:
        heapq.heappush(pq, [-tangerine[i], i])
    
    while pq:
        current = heapq.heappop(pq)
        answer += 1
        cnt += -current[0]
        
        if cnt >= k:
            return answer