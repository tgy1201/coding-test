def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        check = 0
        t = 0
        for j in i:
            if j not in skill:
                continue
            if skill[t] != j:
                check = 1
                break
            else:
                t += 1
        if check == 1:
            continue
        cnt += 1

    return cnt