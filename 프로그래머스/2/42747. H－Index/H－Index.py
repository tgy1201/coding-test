def solution(citations):
    cnt = max(citations)
    
    while True:
        s = list(filter(lambda x: x >= cnt, citations))
        if len(s) >= cnt:
            return cnt
        cnt -= 1