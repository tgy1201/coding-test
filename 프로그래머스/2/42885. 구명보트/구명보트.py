def solution(people, limit):
    people = sorted(people, reverse=True)
    cnt = 0
    start = 0
    end = len(people) -1
    
    while start <= end:
        cnt += 1
        if people[start] + people[end] <= limit:
            end -= 1
        start += 1
            
    return cnt     