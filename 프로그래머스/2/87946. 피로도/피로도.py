from itertools import permutations
def solution(k, dungeons):
    #dungeons = [[80,20],[80,20],[30,10]]
    dd = permutations(dungeons, len(dungeons))
    mm = 0

    for i in dd: #[[80,20],[50,40],[30,10]]
        cnt = 0
        s = k

        for x, y in i: #[80,20]
            if x > s :
                break
            s -= y
            cnt += 1
        
        if mm < cnt:
            mm = cnt
    return mm