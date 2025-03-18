def solution(s):
    dup_s = s * 2
    answer = 0
    
    for i in range(len(s)):
        temp = []
        check = 0
        for j in dup_s[i:i+len(s)]:
            if len(temp) == 0:
                if j == "}" or j == "]" or j ==")":
                    check = 1
                    break
                temp.append(j)
            else:
                if temp[-1] == "{" and j == "}":
                    temp.pop()
                elif temp[-1] == "[" and j == "]":
                    temp.pop()
                elif temp[-1] == "(" and j == ")":
                    temp.pop()
                elif j == "{" or j == "[" or j =="(":
                    temp.append(j)
                else:
                    check = 1
                    break
        if check == 0 and len(temp) == 0:
            answer += 1
    return answer