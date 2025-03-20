def solution(players, m, k):
    answer = 0
    machine = []
    cnt = 0
    
    for i in players:
        if len(machine) == k:
            machine.pop(0)
        if i < m:
            machine.append(0)
        else:
            need = i // m
            temp = sum(machine)
            if temp >= need:
                machine.append(0)
            else:
                machine.append(need-temp)
                answer += need-temp
        
    return answer