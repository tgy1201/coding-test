def solution(n):
    d = {0: "1", 1: "2", 2: "4"}
    aa = ''
    
    def cal124(num, answer):
        if(num-1 < 3):
            answer += d[num-1]
            return answer
        a = (num-1) // 3
        b = (num-1) % 3
        answer += d[b]
        return cal124(a, answer)
    bb = list(cal124(n, aa))
    bb.reverse()
    
    return ''.join(bb)