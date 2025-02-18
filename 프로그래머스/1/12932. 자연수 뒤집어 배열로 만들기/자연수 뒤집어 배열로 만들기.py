def solution(n):
    s = list(str(n))
    answer = [int(s[x]) for x in range(len(s) -1, -1, -1)]
    return answer