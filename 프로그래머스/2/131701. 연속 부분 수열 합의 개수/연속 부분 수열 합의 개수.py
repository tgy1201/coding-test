def solution(elements):
    circle = elements * 2
    dd = []
    
    for index, i in enumerate(elements):
        dd.append(i)
        for j in circle[index+1:index+len(elements)]:
            i += j
            dd.append(i)
    return len(set(dd))

'''
def solution(elements):
    answer = 0
    total = []
    for i in range(1, len(elements)+1):

        for j in range(len(elements)):
            s = 0
            for k in range(j, j+i):
                if k < len(elements):
                    s += elements[k]
                else:
                    s += elements[k%len(elements)]
            total.append(s)
    return len(set(total))
'''