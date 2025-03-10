def solution(files):
    answer = []
    dd = []
    for i in files:
        hc, nc = 0, 0
        head = ''
        number = ''
        tail = ''
        for j in i:
            if not j.isdigit() and hc == 0:
                head+=j
            elif j.isdigit() and nc == 0:
                number+=j
                hc = 1
            else:
                tail+=j
                nc = 1
        dd.append([head, number, tail])
        
        dd = sorted(dd, key=lambda x: (x[0].upper(), int(x[1])))
        
    return [''.join([a,b,c]) for a, b, c in dd]