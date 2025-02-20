def solution(survey, choices):
    answer = 'RCJA'
    d = {"R": 0, "T":0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    p = [3,2,1,0,1,2,3]
    
    for i, v in enumerate(choices):
        if(v < 4):
            d[survey[i][0]] += p[v-1] 
        else:
            d[survey[i][1]] += p[v-1]
    if(d["R"]<d["T"]):
        answer = answer.replace("R","T")
    if(d["C"]<d["F"]):
        answer = answer.replace("C","F")
    if(d["J"]<d["M"]):
        answer = answer.replace("J","M")
    if(d["A"]<d["N"]):
        answer = answer.replace("A","N")
    return answer