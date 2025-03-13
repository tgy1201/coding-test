import heapq
def solution(scoville, K):
    answer = 0
    test = []
    for x in scoville:
        heapq.heappush(test, x)
        
    while True:
        if len(test) <=1 and test[0] < K:
            return -1
        a = heapq.heappop(test)
        
        if a < K:
            answer += 1
            b = heapq.heappop(test)
            c = a + (b*2)
            heapq.heappush(test, c)
        else:
            return answer