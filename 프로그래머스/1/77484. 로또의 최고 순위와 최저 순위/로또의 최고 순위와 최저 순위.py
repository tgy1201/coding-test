def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    cnt = lottos.count(0)
    s = set(win_nums) - set(lottos)
    p = 6 - len(s)
    answer = [rank[p+cnt], rank[p]]
    return answer